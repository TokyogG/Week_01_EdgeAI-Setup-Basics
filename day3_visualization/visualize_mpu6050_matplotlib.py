import polars as pl
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pl.read_parquet("../day2_gpio_mpu/mpu6050_10hz.parquet")

# Use sample index as time axis
ts = np.arange(len(df))

# Extract accel, gyro, temp
ax = df["accel_x_g"]
ay = df["accel_y_g"]
az = df["accel_z_g"]

gx = df["gyro_x_dps"]
gy = df["gyro_y_dps"]
gz = df["gyro_z_dps"]

temp = df["temp_c"]

# === Plotting ===
plt.figure(figsize=(12, 10))

# Accelerometer
plt.subplot(3,1,1)
plt.plot(ts, ax, label="Accel X")
plt.plot(ts, ay, label="Accel Y")
plt.plot(ts, az, label="Accel Z")
plt.title("Accelerometer (g)")
plt.xlabel("Sample")
plt.ylabel("g")
plt.legend()
plt.grid(True)

# Gyroscope
plt.subplot(3,1,2)
plt.plot(ts, gx, label="Gyro X")
plt.plot(ts, gy, label="Gyro Y")
plt.plot(ts, gz, label="Gyro Z")
plt.title("Gyroscope (dps)")
plt.xlabel("Sample")
plt.ylabel("deg/s")
plt.legend()
plt.grid(True)

# Temperature
plt.subplot(3,1,3)
plt.plot(ts, temp, color="orange")
plt.title("Temperature (°C)")
plt.xlabel("Sample")
plt.ylabel("°C")
plt.grid(True)

plt.tight_layout()
plt.show()