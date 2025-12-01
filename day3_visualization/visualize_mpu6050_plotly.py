import polars as pl
import plotly.express as px
import numpy as np

# Load data
df = pl.read_parquet("../day2_gpio_mpu/mpu6050_10hz.parquet")

ts = np.arange(len(df))

df_plot = {
    "ts": ts,
    "accel_x": df["accel_x_g"],
    "accel_y": df["accel_y_g"],
    "accel_z": df["accel_z_g"],
    "gyro_x": df["gyro_x_dps"],
    "gyro_y": df["gyro_y_dps"],
    "gyro_z": df["gyro_z_dps"],
    "temp": df["temp_c"],
}

# Accelerometer plot
fig1 = px.line(
    df_plot,
    x="ts",
    y=["accel_x", "accel_y", "accel_z"],
    title="Accelerometer (g)"
)
fig1.show()

# Gyroscope plot
fig2 = px.line(
    df_plot,
    x="ts",
    y=["gyro_x", "gyro_y", "gyro_z"],
    title="Gyroscope (dps)"
)
fig2.show()

# Temperature plot
fig3 = px.line(
    df_plot,
    x="ts",
    y="temp",
    title="Temperature (°C)"
)
fig3.show()