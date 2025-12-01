# 📦 **Edge Setup Basics – Week 1**

### Raspberry Pi 5 + Hailo-8L Bootcamp

*GPIO • I²C Sensors • IMU Visualization • Parquet Logging • Streamlit Dashboard • ONNX Export*

---

# 🧭 Overview

This repository contains all work completed in **Week 1** of the *Edge AI Bootcamp* using:

* **Raspberry Pi 5 (8GB)**
* **Hailo-8L M.2 Accelerator + Hailo M.2 HAT**
* **MPU6050 IMU (I²C)**
* **LED + Resistor**
* **Python 3.11 (`edge_bootcamp` venv)**

Week 1 focuses on:

* Setting up the Raspberry Pi as a development workstation
* Building basic GPIO and I²C sensor interactions
* Logging IMU data in Parquet format
* Creating real-time visualizations (ASCII + Streamlit Dashboard)
* Running a modern analytics workflow on the Pi
* Exporting your first ONNX model
* Organizing results into a clean, portfolio-ready repo

This repo is **Repo #0** in the 16-week bootcamp.

---

# 📅 **Week 1 Summary (Final Updated Structure)**

> NOTE: Day 2 has been split into a hardware day and a visualization day.
> This gives a more natural flow and significantly improves student learning.

---

## **Day 1 – Raspberry Pi Setup & Development Environment**

* Installed Raspberry Pi OS 64-bit
* Enabled SSH + VS Code Remote Development
* Created Python virtualenv `edge_bootcamp`
* Installed essential packages (gpiozero, RPi.GPIO, smbus2, torch, polars, pyarrow, onnx, streamlit)
* Enabled I²C and verified device tree access
* Collected system info (`lscpu`, `free -h`, `uname -a`, `lsblk`, `lspci`)
* Set up Git identity and repo initialization

**Outcome:** Pi is fully ready for hardware + ML development.

---

## ⭐ **Day 2 – GPIO + IMU Hardware + Sensor Logging**

### ✔ GPIO LED Blink

* LED on GPIO17
* Discovered **critical Hailo M.2 HAT GPIO limitation:**
  The HAT header does **not** expose real Pi GPIO pins
* Performed jumper-wire workaround to break out 3V3, GND, GPIO17, SDA, SCL

### ✔ MPU6050 IMU Setup (I²C)

* Wired using 3.3V, GND, SDA (Pin 3), SCL (Pin 5)
* Verified with `i2cdetect -y 1`

### ✔ IMU Logging to Parquet

* `mpu6050_logger.py` logs accel/gyro/temp at ~10 Hz
* Produces `mpu6050_10hz.parquet` automatically

### ✔ ASCII Live Motion Monitor

* Real-time tilt visualization directly in terminal
* Fun and highly educational

### ✔ quick_stats.py (Polars)

* Mean, std, min/max
* Accel magnitude
* Tilt clues
* Sampling rate estimate

**Outcome:** Real hardware → real data → clean Parquet logs.

---

## ⭐ **Day 3 – Data Visualization & Streamlit Dashboard**

Using real IMU logs collected in Day 2.

### ✔ Matplotlib visualization

* accel_x/y/z vs time
* gyro_x/y/z vs time
* temp vs time

### ✔ Plotly interactive charts

* zoom, hover, panning
* browser-based plots

### ✔ Streamlit IMU Dashboard

A full GUI dashboard:

* Accelerometer charts
* Gyroscope charts
* Temperature
* Accel magnitude
* Tilt angle
* Rolling window smoothing
* Stats summary
* File selector auto-discovery of `.parquet` files

Launch:

```bash
cd ~/Week_01_EdgeAI-Setup-Basics/day3_visualization
streamlit run imu_dashboard.py
```

In your **laptop browser**:

```
http://<raspberry-pi-ip>:8501
```

Streamlit prints:

* Local URL → ignore
* External URL → ignore (won’t work behind home router)
* **Network URL ("192.168.x.x") → USE THIS**

**Outcome:** Students now have a real IMU analytics dashboard running on the Pi.

---

## ⭐ **Day 4 – PyTorch → ONNX Export**

* Created `TinyModel` in PyTorch
* Exported to ONNX with:

```python
torch.onnx.export(...)
```

* Encountered opset auto-upgrade (17→18)
* Valid `.onnx` file generated successfully

**Outcome:** First working ONNX export pipeline.

---

## ⭐ **Day 5 – Repo Organization + Benchmarks**

* Organized folders by day
* Added wiring diagrams
* Added “Hailo GPIO issue” documentation
* Benchmarks:

  * Logger RAM < 100 MB
  * ONNX export time
  * CSV vs Parquet file sizes
* Clean README + documentation
* Repo now polished, portfolio-ready

---

# 📁 **Repo Structure**

```
edge-setup-basics/
│
├── day1_setup/
│   ├── notes.md
│   └── system_info.txt
│
├── day2_gpio_mpu/
│   ├── blink_led.py
│   ├── mpu6050_logger.py
│   ├── mpu6050_monitor.py
│   ├── mpu6050_ascii_monitor.py
│   ├── quick_stats.py
│   ├── quick_stats.md
│   ├── hailo_m2hat_gpio_notes.md
│   ├── wiring_diagram_led.md
│   └── wiring_diagram_mpu6050.md
│
├── day3_visualization/
│   ├── visualize_mpu6050_matplotlib.py
│   ├── visualize_mpu6050_plotly.py
│   ├── imu_dashboard.py
│   └── imu_data_visualization.md
│
├── day4_onnx_export/
│   ├── dummy_to_onnx.py
│   ├── tiny_model.onnx
│   └── export_logs.txt
│
├── benchmarks/
│   ├── logger_ram_usage.txt
│   ├── parquet_vs_csv_sizes.md
│   └── onnx_export_timing.md
│
├── env/
│   ├── requirements.txt
│   └── venv_notes.md
│
├── images/
│   └── streamlit_dashboard_sample.png
│
└── README.md   <-- (this file)
```

---

# 🌟 **Key Learnings (Moat for Future Course)**

* Hailo GPU/GPIO conflict is a unique hardware limitation
* Real IMU data pipelines create powerful teaching examples
* Streamlit dashboards make the course feel modern & industry-aligned
* Students now understand:

  * GPIO
  * I²C
  * Real-time logging
  * IMU interpretation
  * Statistics
  * Dashboards
  * ONNX export
  * Repo organization

The bootcamp now delivers **hands-on hardware, data engineering, and edge AI foundations** — all in Week 1.

---

# 🚀 **Next Week (Week 2 Preview)**

**Modern Data Pipelines + Performance**

* Polars vs Pandas benchmarks
* Real-time logging to dashboard
* Performance profiling
* Quantization fundamentals
* INT8 model benchmark
* Notebook + script pipelines
* Repo #1: `edge-pipelines`