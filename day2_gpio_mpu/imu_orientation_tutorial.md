# 🧭 Understanding IMU Orientation (MPU6050)
*A practical guide for beginners who want to understand accelerometer and gyroscope data.*

The MPU6050 is a 6-axis IMU:
- 3-axis accelerometer  
- 3-axis gyroscope  

This tutorial explains how to interpret the values.

---

# 1. Coordinate Axes (Right-Hand Rule)

Most IMUs, including the MPU6050, follow this orientation:


   +Z
   ↑
   |
   O------→ +X
  /
 /


+Y


- **+X**: forward  
- **+Y**: left  
- **+Z**: upward  

Your module may be rotated — that’s part of the learning.

---

# 2. Accelerometer Basics

Accelerometer measures **specific force**, not velocity.

When resting flat:



accel_x ≈ 0 g
accel_y ≈ 0 g
accel_z ≈ +1 g (gravity)


Tilt the IMU:

- Rotate forward → +X increases  
- Rotate sideways → +Y changes  
- Flip upside-down → Z becomes −1 g  

### Accel Magnitude



sqrt(x² + y² + z²) ≈ 1 g


If this is far from 1:
- sensor is accelerating
- strong vibration
- calibration is off
- the data format is incorrect

---

# 3. Gyroscope Basics

Gyroscope measures **angular velocity** in degrees per second (dps).

When still:



gyro_x ≈ 0
gyro_y ≈ 0
gyro_z ≈ 0


Rotate around an axis → that axis spikes:

- Rotate around X → `gyro_x_dps` changes  
- Rotate around Y → `gyro_y_dps` spikes  
- Spin on table → `gyro_z_dps` large  

Gyro is great for:
- short-term orientation
- smooth motion
- gesture recognition
- vibration detection

But gyro drifts → why we need filtering (next doc).

---

# 4. Interpreting Your Quick Stats Output

Example from your real MPU6050:



Accel Z: mean=0.977 g
Accel magnitude: 1.029 g


This tells us:
- Sensor is upright  
- Gravity mostly aligned with +Z  
- Small noise (std=0.081)  

Gyro example:



Gyro Y: min=-199 dps, max=135 dps


You rotated strongly around Y — makes sense for handheld testing.

---

# 5. Common IMU Pitfalls

### ❌ Confusing m/s² and g  
Your data is in **g**, not m/s².

### ❌ Expecting exact 0 or 1  
IMU values always jitter.

### ❌ Using gyro for absolute angle  
Gyro **drifts** over time.

### ❌ Forgetting orientation  
You must know which axis points where.

---

# 6. What’s Next?

Understanding IMU basics prepares you for:

- Noise filtering (next guide)  
- Motion classification  
- Embedded ML  
- Gesture recognition  
- Vibration analysis  

The IMU is one of the richest sensors in edge AI — mastering orientation is essential.