# 🌀 IMU Filtering Guide
*A gentle introduction to filtering accelerometer + gyroscope data.*

Raw IMU data:
- is noisy  
- drifts  
- conflicts between accelerometer & gyro  
- is not ready for ML or robotics  

We need filters.

This guide explains **three essential IMU filters** used everywhere in drones, robots, AR/VR, and edge AI.

---

# 1. Why Filtering Is Needed

Accelerometer:
- Good long-term reference (gravity)
- Bad short-term (jittery)
- Sensitive to vibration

Gyroscope:
- Excellent short-term stability (smooth)
- Horrible long-term drift  
- Bias accumulates → orientation becomes wrong

Thus:



accel = long-term truth
gyro = short-term stability


Filtering = fuse them.

---

# 2. Complementary Filter (Beginner Friendly)

This is the simplest useful filter:



angle = α * (angle + gyro * dt) + (1 - α) * accel_angle


Where:
- gyro gives fast changes  
- accel corrects slow drift  
- α is usually ~0.98  

### Pros:
- Very easy to code  
- No matrix math  
- Great for low-power MCUs  
- Works well for tilt angles  

### Cons:
- Not as robust as Kalman  
- Assumes simple motion  

### Perfect for:
- Pi projects  
- IoT sensors  
- Gestures  
- Robotics 101  

---

# 3. Kalman Filter (Advanced but Powerful)

Kalman filters are used in:
- drones  
- self-driving cars  
- INS/GNSS systems  
- aerospace  

Kalman maintains:
- a prediction model  
- a measurement model  
- uncertainty covariance  
- optimal correction  

### Pros:
- Extremely accurate  
- Handles noise probabilistically  
- Industry standard  

### Cons:
- More math  
- Harder to tune  
- Not needed for simple tilt demos  

### Perfect for:
- Orientation estimation  
- Sensor fusion  
- Navigation  
- Week 11–12 vibration ML (later in bootcamp)

---

# 4. Madgwick / Mahony Filters (Quaternion-Based)

These are popular in hobby IMUs and VR controllers.

### Madgwick Filter
Uses gradient descent to estimate orientation quaternions.

### Mahony Filter
Uses PI-control style correction.

### Pros:
- Very fast  
- Works on MCUs  
- Produces stable 3D orientation  
- Better than complementary filter in 3D  

### Cons:
- More complex than complementary  
- Not as theoretically clean as Kalman  

### Perfect for:
- VR/AR  
- Robotics and drones  
- Full 3D tracking  
- IMUs with magnetometers  

---

# 5. Which Filter Should Students Learn First?

For this bootcamp:

### Week 2–5  
👉 **Complementary filter**

Works perfectly with:
- MPU6050  
- Pi 5  
- early projects  
- tilt visualization  
- ASCII monitor upgrades

### Week 11–12  
👉 **Kalman + spectral analysis**  
For:
- vibration classification  
- anomaly detection  
- sensor fusion models  

### Later / Optional  
👉 **Madgwick/Mahony** for full 3D projects.

---

# 6. Suggested Student Labs

- Add a complementary filter to smooth ASCII tilt  
- Implement gyro-integrated tilt vs accel tilt  
- Compare filtered vs unfiltered noise  
- Rotate sensor and watch drift  
- Add high-frequency vibration and analyze FFT  
- Show difference between 10 Hz and 100 Hz sampling  

---

# 7. Summary Table

| Filter | Difficulty | Performance | Use Case |
|--------|------------|-------------|----------|
| Complementary | ⭐ Easy | Good | Tilt, beginners |
| Kalman | ⭐⭐⭐ Hard | Excellent | Navigation, fusion |
| Madgwick/Mahony | ⭐⭐ Medium | Very Good | 3D orientation |

