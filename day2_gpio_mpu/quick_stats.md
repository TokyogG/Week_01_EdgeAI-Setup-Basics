# 📊 **Quick Stats for IMU Data (quick_stats.py)**

### *Intro to Basic Statistics Using Real Sensor Data*

This document explains how to use the `quick_stats.py` tool to get fast, meaningful insights from MPU6050 IMU logs. It also introduces fundamental statistical concepts that every Edge AI / IoT engineer should know.

---

# 🧭 What This Tool Does

`quick_stats.py` provides a **quick overview** of a recorded dataset by computing:

* **Mean**
* **Standard deviation**
* **Minimum & Maximum**
* **Accelerometer magnitude** (gravity alignment)
* **Estimated sample rate** (if timestamps available)

It is designed to:

* Help beginners understand sensor behavior
* Validate that the IMU is wired correctly
* Check whether data is “good” before building pipelines
* Provide intuition for later ML steps (filters, anomalies, features)

---

# 🚀 How to Use It

Run the script from the `day2_gpio_mpu/` folder:

```bash
python quick_stats.py <your_file.parquet or .csv>
```

Example:

```bash
python quick_stats.py mpu6050_10hz.parquet
```

---

# 📁 Supported File Formats

* `.parquet` (recommended — fast and compact)
* `.csv`

The script automatically detects the format based on filename extension.

---

# 📌 Columns Expected

The script looks for these IMU columns:

* `accel_x_g`, `accel_y_g`, `accel_z_g`
* `gyro_x_dps`, `gyro_y_dps`, `gyro_z_dps`
* `temp_c`
* `timestamp` (optional)

If any columns are missing, they are simply skipped.

---

# 📈 Sample Output (From Real MPU6050 Run)

Below is an example using your **10 Hz, 10-second** MPU6050 capture.

```
=== Quick Stats (Polars) ===

Accel X: mean=0.043  std=0.296  min=-0.516  max=0.683
Accel Y: mean=-0.032  std=0.101  min=-0.281  max=0.177
Accel Z: mean=0.977  std=0.081  min=0.700  max=1.150
Gyro X: mean=-1.856  std=22.911  min=-62.168  max=62.275
Gyro Y: mean=-1.403  std=49.051  min=-199.740  max=135.618
Gyro Z: mean=-0.464  std=5.089  min=-15.198  max=11.580
Temperature (°C): mean=24.442  std=0.417  min=23.730  max=25.189

Accel magnitude (avg): 1.029 g

=== End Stats ===
```

---

# 🧠 What These Stats Tell Us

### ✔ Accelerometer

* Z ≈ **0.98 g** → sensor is upright, aligned with gravity
* X & Y ≈ **0** → level, not tilted
* std is low → stable, low vibration
* magnitude ≈ **1.03 g** → correct calibration

### ✔ Gyroscope

* Means are near 0 → no major rotational drift
* Higher std/min/max → shows active rotations during capture
* Y-axis spikes (±200 dps) → you rotated around Y most

### ✔ Temperature

* Mean ≈ **24.4°C**, std very small
* Indicates stable room temperature and sensor thermals

This teaches students how to interpret IMU noise, bias, and orientation.

---

# 📘 Why This Matters in an Edge AI Bootcamp

### 1. **Builds Early Intuition**

Before using filters (Kalman, complementary) or ML models, students need to understand what IMU values *look like*.

### 2. **Catches Wiring & Logic Errors**

If accel magnitude ≠ ~1 g → orientation or wiring is wrong.
If gyro std is nearly 0 → IMU may not be updating.

### 3. **Prepares for ML Pipelines**

Statistical features (mean, std, max, range) are used in:

* Gesture recognition
* Vibration analysis
* Anomaly detection
* Edge ML models (Week 11–12)

### 4. **Makes the course feel premium**

This is exactly the kind of “extra tool” that elevates a bootcamp.

---

# 🧱 Next Steps

* Use `quick_stats.py` on your own MPU6050 captures
* Try recording with stronger movement and compare the stats
* Try leaving the IMU still for 10 seconds — see how noise looks
* Later: compute rolling stats, variance windows, FFTs
* Feed stats into TinyML models (Weeks 11–12)