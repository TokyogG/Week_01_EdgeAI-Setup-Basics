import streamlit as st
import polars as pl
import numpy as np
from pathlib import Path

# ---------- Page config ----------
st.set_page_config(page_title="MPU6050 IMU Dashboard", layout="wide")

st.title("📊 MPU6050 IMU Dashboard")
st.write("Visualizing real accelerometer, gyroscope, and temperature data from the Raspberry Pi.")

# ---------- Data selection ----------
# Directory where parquet files are stored (explicit path on the Pi)
DATA_DIR = Path.home() / "Week_01_Edge-Setup-Basics" / "day2_gpio_mpu"

st.sidebar.header("Data Source")
st.sidebar.write(f"Looking for .parquet files in:\n`{DATA_DIR}`")

parquet_files = sorted(DATA_DIR.glob("*.parquet"))

if not parquet_files:
    st.sidebar.error(f"No .parquet files found in {DATA_DIR}")
    st.stop()

file_options = [f.name for f in parquet_files]

selected_name = st.sidebar.selectbox(
    "Select a .parquet file from the Pi",
    file_options,
    index=0,
)
selected_file = DATA_DIR / selected_name
st.sidebar.success(f"Using local file: {selected_name}")

# ---------- Load data ----------
df = pl.read_parquet(selected_file)
st.write(f"Loaded **{len(df)}** rows from `{selected_file}`")

# Convert to pandas for Streamlit charts
df_pd = df.to_pandas()

# ---------- Derived features ----------
# Accel magnitude
ax = df_pd["accel_x_g"]
ay = df_pd["accel_y_g"]
az = df_pd["accel_z_g"]
df_pd["accel_mag"] = np.sqrt(ax * ax + ay * ay + az * az)

# Tilt angle (degrees) using accel only
df_pd["tilt_deg"] = np.degrees(np.arctan2(df_pd["accel_y_g"], df_pd["accel_z_g"]))

# Sidebar control for rolling window
window = st.sidebar.slider("Rolling window size (samples)", 1, 50, 10)
df_pd["accel_mag_roll"] = df_pd["accel_mag"].rolling(window).mean()

# ---------- Layout ----------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Accelerometer (g)")
    st.line_chart(df_pd[["accel_x_g", "accel_y_g", "accel_z_g"]])

    st.subheader("Accel Magnitude (g)")
    st.line_chart(df_pd[["accel_mag", "accel_mag_roll"]])

with col2:
    st.subheader("Gyroscope (dps)")
    st.line_chart(df_pd[["gyro_x_dps", "gyro_y_dps", "gyro_z_dps"]])

    st.subheader("Temperature (°C)")
    st.line_chart(df_pd["temp_c"])

st.subheader("Tilt Angle (degrees)")
st.line_chart(df_pd["tilt_deg"])

st.subheader("Quick Stats (describe)")
st.dataframe(df_pd.describe())
