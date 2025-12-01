# **Day 1 – Setup Notes**

**Date:** Week 1 – Day 1
**Project:** Edge AI Bootcamp (Raspberry Pi 5 + Hailo 8L)

---

# 1. Raspberry Pi OS Setup

**OS Installed:** Raspberry Pi OS 64-bit
**Device:** Raspberry Pi 5 (8GB)

Steps:

	1. Flashed OS using Raspberry Pi Imager
	2. Enabled:
	   * SSH
	   * Wi-Fi (or Ethernet)
	* Default username/password
	3. Booted Pi and performed system updates:
		sudo apt update && sudo apt upgrade -y
---

# 🔌 2. Remote Development Setup

## **SSH Access**

Tested connection from main machine: ssh pi@<raspberrypi.local or IP>
```

## **VS Code Remote SSH**

Installed extension:

* **Remote – SSH**

Connected VS Code to the Pi: Remote Explorer → SSH Targets → raspberrypi.local

---

# 3. Python Environment

Created Python virtual environment for this bootcamp: python3 -m venv edge_bootcamp

Activated: source edge_bootcamp/bin/activate

Installed core packages:
	pip install --upgrade pip
	pip install numpy pandas pyarrow matplotlib gpiozero RPi.GPIO smbus2
	pip install torch onnx

Notes:

* This venv is where all GPIO, I²C, and ONNX tools live

---

# 4. Essential Tools Installed

sudo apt install -y git python3-venv python3-dev python3-pip \
                   lshw i2c-tools neofetch

Enabled I²C:

sudo raspi-config

Navigate: Interface Options → I2C → Enable

Check MPU6050 visibility: i2cdetect -y 1

---

# 5. System Information Commands

These commands were used to collect hardware and OS info.

## CPU: lscpu
## Memory: free -h
## OS Version:  cat /etc/os-release
## Kernel:  uname -a
## Model & Revision: 	cat /proc/device-tree/model
			cat /proc/cpuinfo | grep Revision
## Storage: 	df -h
		lsblk
## PCIe (important for Hailo M.2): lspci
## USB devices: lsusb

To dump all to file (optional):

```bash
(
echo "===== CPU ====="; lscpu;
echo "===== MEM ====="; free -h;
echo "===== OS ====="; cat /etc/os-release;
echo "===== KERNEL ====="; uname -a;
echo "===== MODEL ====="; cat /proc/device-tree/model;
echo "===== REVISION ====="; cat /proc/cpuinfo | grep Revision;
echo "===== STORAGE ====="; df -h;
echo "===== LSBLK ====="; lsblk;
echo "===== PCIe ====="; lspci;
echo "===== USB ====="; lsusb;
) > system_info.txt
```

---

# 6. Git Setup

Configured Git identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

Initialized repo:

```bash
git init
```

---

# 7. Notes & Observations

* Pi 5 runs much cooler than expected with passive cooling
* SSH + VS Code remote workflow is smooth
* Virtual environment activated fine and GPIO-level permissions work
* Hailo M.2 card visible via `lspci`
* Ready to begin GPIO + I²C (Day 2)
