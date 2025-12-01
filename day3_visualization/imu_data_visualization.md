# 📊 **Day 3 – IMU Data Visualization & Dashboarding**

*Using Real Sensor Data from Day 2*

Day 3 builds on the real hardware logging you completed in Day 2.
Today you’ll learn how to:

* Load the IMU data you captured from the MPU6050
* Visualize accelerometer, gyroscope, and temperature signals
* Inspect derived features like magnitude and tilt
* Build a **Streamlit dashboard** to interactively explore the data

Visualization is a critical skill in edge AI. Before you can train a model or detect anomalies, you need to *see* and *understand* your signals.

---

# 🧭 1. Data Loading (Polars)

All Day 3 tools expect a Parquet file produced by Day 2’s logger:

```
day2_gpio_mpu/mpu6050_10hz.parquet
```

Load it with Polars:

```python
import polars as pl
df = pl.read_parquet("mpu6050_10hz.parquet")
```

This gives you ~95 rows from a 10-second, 10 Hz capture.

---

# 🖼️ 2. Visualization Tools

### ✔ `visualize_mpu6050_matplotlib.py`

Classic signal plots (accel, gyro, temperature)

### ✔ `visualize_mpu6050_plotly.py`

Interactive zoomable plots (hover values, tooltips, pan)

### ✔ `imu_dashboard.py` (**Streamlit**)

A full browser-based dashboard with:

* Accelerometer line charts
* Gyroscope line charts
* Temperature chart
* Rolling mean smoothing
* Accel magnitude
* Tilt angle
* Statistics table
* Drop-down file selection

This is the most modern way to explore IMU data and is used in real IoT / Edge AI systems.

---

# 🌐 3. Launching the Streamlit Dashboard

This is the part where students commonly get confused, so we spell it out clearly.

### ▶️ Step 1 — Run Streamlit on the Pi

SSH into your Pi:

```bash
cd ~/edge-setup-basics/day3_visualization
streamlit run imu_dashboard.py
```

Streamlit will print something like:

```
Local URL: http://localhost:8501
Network URL: http://192.168.0.87:8501
External URL: http://192.226.226.112:8501
```

### ‼️ Important Notes

* **Use the Network URL** → `http://192.168.x.x:8501`
  This is the URL you open **on your laptop browser**.

* **Ignore the External URL**
  It usually won’t work without router port-forwarding or public IP routing.

* The Local URL is only for when you run a browser directly on the Pi.

---

# 🖥️ 4. Opening the Dashboard in Your Browser

From your **laptop**, open the LAN URL:

```
http://192.168.0.87:8501
```

You should see the full dashboard:

![Streamlit Dashboard Screenshot](../images/streamlit_dashboard_sample.png)

*(Use your screenshot; place it under `/images` and adjust path if needed.)*

The dashboard auto-detects all `.parquet` files in:

```
~/edge-setup-basics/day2_gpio_mpu/
```

And loads the selected dataset automatically.

---

# 📈 5. What You’ll See in the Dashboard

### Accelerometer (g)

Shows tilt and gravity balance across X, Y, Z.

### Gyroscope (dps)

Spikes correspond to rotation intensity.

### Temperature (°C)

Shows IMU heat stability.

### Accel Magnitude

Should hover close to **1 g** when stationary.

### Tilt Angle (degrees)

Estimates pitch angle using only accelerometer axis ratios:

```
tilt = atan2(accel_y, accel_z)
```

### Rolling Window Smoothing

The sidebar slider lets you smooth out noise with a rolling mean.

### Stats Summary

Interactive `describe()` table from your data.

---

# 🎓 6. Student Exercises (Recommended)

1. **Wave the IMU faster** and see how gyro spikes change.
2. **Tilt the sensor 90°** and watch accel Z drop to near 0.
3. **Add high-frequency vibration** (tap the table) and watch accel magnitude jitter.
4. Try different `"window"` values in the sidebar.
5. Capture a second Parquet file and compare them.

---

# 🧠 7. Why This Matters in Industry

Dashboards like this are used in:

* Predictive maintenance
* Remote monitoring
* Health diagnostics for machines
* Robotics debugging
* Data validation before ML model training
* Feature engineering for classification models

This tool gives you a **modern workflow** that is directly transferable to real jobs.

---

# 📌 8. Folder Structure

Day 3 files live here:

```
day3_visualization/
    visualize_mpu6050_matplotlib.py
    visualize_mpu6050_plotly.py
    imu_dashboard.py
    imu_data_visualization.md   <-- this file
```

---

# 🚀 9. Next Step: Day 4 – ONNX Export

Tomorrow you export your first model from PyTorch to ONNX, ready for edge deployment.