import sys
import polars as pl
import numpy as np

def quick_stats(df):
    print("\n=== Quick Stats (Polars) ===\n")

    # List of IMU columns with display names
    sensors = [
        ("accel_x_g", "Accel X"),
        ("accel_y_g", "Accel Y"),
        ("accel_z_g", "Accel Z"),
        ("gyro_x_dps", "Gyro X"),
        ("gyro_y_dps", "Gyro Y"),
        ("gyro_z_dps", "Gyro Z"),
        ("temp_c", "Temperature (°C)"),
    ]

    # Calculate and print stats for each existing column
    for col, name in sensors:
        if col in df.columns:
            stats = df.select(
                pl.col(col).mean().alias("mean"),
                pl.col(col).std().alias("std"),
                pl.col(col).min().alias("min"),
                pl.col(col).max().alias("max")
            ).to_dict(as_series=False)

            print(f"{name}: mean={stats['mean'][0]:.3f}  "
                  f"std={stats['std'][0]:.3f}  "
                  f"min={stats['min'][0]:.3f}  "
                  f"max={stats['max'][0]:.3f}")

    # Accel magnitude (gravity estimate)
    if all(c in df.columns for c in ["accel_x_g", "accel_y_g", "accel_z_g"]):
        ax = df["accel_x_g"].to_numpy()
        ay = df["accel_y_g"].to_numpy()
        az = df["accel_z_g"].to_numpy()
        mag = np.sqrt(ax*ax + ay*ay + az*az)
        print(f"\nAccel magnitude (avg): {mag.mean():.3f} g")

    # Estimate sample rate if timestamp appears numeric
    if "timestamp" in df.columns:
        try:
            ts = df["timestamp"].cast(pl.Float64).to_numpy()
            dt = np.diff(ts)
            sr = 1.0 / np.mean(dt)
            print(f"Estimated sample rate: {sr:.2f} Hz")
        except:
            pass

    print("\n=== End Stats ===\n")


if __name__ == "__main__":
    # Require an input file from the user
    if len(sys.argv) < 2:
        print("Usage: python quick_stats.py <datafile.parquet or .csv>")
        sys.exit(1)

    filename = sys.argv[1]

    # Load using Polars
    if filename.endswith(".parquet"):
        df = pl.read_parquet(filename)
    elif filename.endswith(".csv"):
        df = pl.read_csv(filename)
    else:
        print("Error: file must be .parquet or .csv")
        sys.exit(1)

    quick_stats(df)
