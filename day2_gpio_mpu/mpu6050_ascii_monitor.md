# 🎮 MPU6050 ASCII Live Motion Monitor
*A simple, fun way to visualize IMU motion directly from the terminal.*

This document explains how the ASCII-based live monitor works, why it is useful, and what students learn from it.

---

# 🧭 What This Tool Does

The ASCII monitor displays **real-time accelerometer-based tilt** using only text.

Example output:



ACC X: -0.12 Y: 0.03 Z: 9.80
Tilt:
/
/
----O----
/
/


It updates continuously at ~10 Hz (or whatever rate your MPU6050 is sampling).

This creates a *terminal-based visualization* of how the IMU is moving.

---

# 📦 How It Works

### 1. Read accelerometer values  
From the MPU6050:
- `accel_x_g`
- `accel_y_g`
- `accel_z_g`

### 2. Normalize to get tilt direction  
We convert X/Y tilt into an angle:



tilt_angle = arctan2(accel_y_g, accel_z_g)


### 3. Map angle to ASCII characters  
A simple set of rules:

- Angle near 0° → horizontal (“----O----”)  
- Angle positive → tilt left (`\`)  
- Angle negative → tilt right (`/`)

### 4. Refresh display  
Uses `print("\033c")` or back-to-back prints to redraw the frame.

---

# 🎓 What Students Learn

This is an excellent teaching tool because it shows:

### ✔ How accelerometers react to gravity  
When the IMU is still:
- Z ≈ 1 g  
- X, Y ≈ 0 g

### ✔ How tilt changes X/Y  
Rotate it around X → Y changes  
Rotate it around Y → X changes

### ✔ That sensors are noisy  
Even at rest, values "jitter" due to:
- electrical noise  
- temperature  
- vibration  
- quantization error  

### ✔ Real-time feedback is motivating  
Students *see* their motion on screen — very interactive.

---

# 📌 Suggested Student Challenges

- Add a “compass needle” style ASCII visualization  
- Add a rolling average to reduce jitter  
- Add colors using ANSI escape codes  
- Try 20 Hz sampling and compare responsiveness  
- Add gyro-based rotation estimation  

---

# 🧠 Why This Matters (Bootcamp Perspective)

ASCII visualization requires:
- no GUI  
- no OpenCV  
- no extra libraries

Yet it teaches:
- live loops  
- sensor sampling  
- data normalization  
- visualization logic  
- tilt physics  