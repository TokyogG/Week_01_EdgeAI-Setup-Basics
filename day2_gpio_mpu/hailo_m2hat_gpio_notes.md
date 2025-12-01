This file documents the hardware issue regarding the setup of the M2 Hat on the Pi5:

---

# ⚠️ **Hailo M.2 HAT GPIO Notes**

**File:** `day2_gpio_mpu/hailo_m2hat_gpio_notes.md`
**Purpose:** Document unexpected hardware behavior of the Hailo M.2 HAT GPIO header and the workaround.

---

# ⚠️ Summary

The **GPIO header on the Hailo M.2 HAT does *not* expose the Raspberry Pi GPIO pins** as labeled on the Pi pinout.
This means:

* Standard Raspberry Pi GPIO tutorials will **NOT work**
* The pins on the Hailo HAT header are **not electrically connected** to the Pi’s GPIO pins
* Attempts to blink an LED using these pins will fail
* This affects **all GPIO tasks (Day 2 LED blink, PWM, sensors, interrupts, etc.)**

This is a **non-obvious hardware limitation** that will surprise most users.

---

# 🔍 What We Observed

* LED blink code ran fine, but **Hailo HAT pins never toggled voltage**
* GPIO17, GPIO27, GPIO22 all showed **No Output** on the HAT header
* But the same code **worked perfectly** when wired directly to the raw Pi GPIO header

This confirms the Hailo HAT GPIO header is either:

* Not connected
* Mapped to a different device
* Reserved for Hailo functionality
* Or not meant for Raspberry Pi GPIO at all

---

# 🛠️ Workaround (Successful)

To use real Raspberry Pi GPIO pins:

### ✔ Cut jumper wire plug head to reduce height of jumper head
### ✔ Gently bend wire so it comes out the side of the Raspberry Pi Unit.  
### ✔ Cut opening in the side of Raspberry Pi Case to allow wires to come out



open a gap in the HAT case

The HAT sits directly above the Pi GPIO header, blocking access.

### ✔ Manually expose 5 real Pi GPIO pins

We pulled out:

* **3.3V**
* **GND**
* **GPIO17** (Pin 11)
* **GPIO2 / SDA1** (Pin 3)
* **GPIO3 / SCL1** (Pin 5)

### ✔ Used jumper wires to route these to a breadboard

From there we connected:

* LED + resistor
* MPU6050 via I²C
* Future sensors

After doing this, **all GPIO functions worked as expected.**

---

# 📌 Why This Matters (Moat Insight)

This issue adds **real value** to our bootcamp/documentation:

### ✔ Most online tutorials assume direct access to Pi GPIO

With the Hailo HAT, that is not possible.

### ✔ This is a pain point that can be productized:

* A **custom GPIO breakout** for Pi 5 + Hailo
* A **premium bootcamp** with this workaround documented
* A **troubleshooting guide** unique to this hardware combo
* A **pre-configured kit** that avoids the problem

This becomes part of the **competitive moat** of the course.

---

# 📐 Correct Wiring After Applying Workaround

### LED Wiring (GPIO17):

```
GPIO17 (Pin 11 on Pi header) ───► Resistor ───► LED +  
LED - ───► GND (Pin 6)
```

### MPU6050 Wiring (I²C):

```
3.3V  → VCC
GND   → GND
SDA   → SDA1 (Pin 3)
SCL   → SCL1 (Pin 5)
```

These connections are **from the Pi directly**, NOT from the Hailo HAT header.

---

# 🧪 How We Verified It

1. Used `gpiozero` and `RPi.GPIO` to toggle GPIO17
2. Confirmed LED did NOT blink when connected to Hailo HAT pins
3. Connected to direct Pi header → LED blinked correctly
4. Verified GPIO output using:

```
gpio readall
```

and a multimeter.

---

# 📝 Conclusion

**The Hailo M.2 HAT GPIO header is not usable for Raspberry Pi GPIO work.**
Use jumper wires directly from the Pi 5 GPIO header for all:

* LEDs
* Sensors
* PWM
* I²C devices
* GPIO-based projects in this bootcamp

This documentation ensures future students avoid the same pitfall.

---

If you want, I can also generate:

* `wiring_diagram_led.md`
* `wiring_diagram_mpu6050.md`
* Cleaned versions of all Day 2 scripts

Just tell me!
