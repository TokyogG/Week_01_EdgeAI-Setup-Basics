import time
from datetime import datetime

import polars as pl
from smbus2 import SMBus

MPU_ADDR = 0x68  # I2C address when AD0 is tied to GND

# MPU6050 register addresses
PWR_MGMT_1    = 0x6B
ACCEL_XOUT_H  = 0x3B
TEMP_OUT_H    = 0x41
GYRO_XOUT_H   = 0x43

LOG_FREQ_HZ = 10
INTERVAL = 1.0 / LOG_FREQ_HZ
DURATION_SEC = 10  # how long to log
OUTPUT_FILE = "mpu6050_10hz.parquet"


def read_word(bus, addr, reg):
    """Read a 16-bit signed value from two 8-bit registers."""
    high = bus.read_byte_data(addr, reg)
    low = bus.read_byte_data(addr, reg + 1)
    value = (high << 8) | low
    # Convert to signed
    if value >= 0x8000:
        value = -((65535 - value) + 1)
    return value


def main():
    records = []

    with SMBus(1) as bus:
        # Wake up MPU6050 (clear sleep bit)
        bus.write_byte_data(MPU_ADDR, PWR_MGMT_1, 0x00)
        time.sleep(0.1)

        print(f"Logging MPU6050 at {LOG_FREQ_HZ} Hz for {DURATION_SEC} seconds...")
        start = time.time()

        while (time.time() - start) < DURATION_SEC:
            ts = datetime.utcnow().isoformat()

            # Raw readings
            accel_x_raw = read_word(bus, MPU_ADDR, ACCEL_XOUT_H)
            accel_y_raw = read_word(bus, MPU_ADDR, ACCEL_XOUT_H + 2)
            accel_z_raw = read_word(bus, MPU_ADDR, ACCEL_XOUT_H + 4)

            temp_raw    = read_word(bus, MPU_ADDR, TEMP_OUT_H)

            gyro_x_raw  = read_word(bus, MPU_ADDR, GYRO_XOUT_H)
            gyro_y_raw  = read_word(bus, MPU_ADDR, GYRO_XOUT_H + 2)
            gyro_z_raw  = read_word(bus, MPU_ADDR, GYRO_XOUT_H + 4)

            # Convert to physical units (default ±2g, ±250°/s)
            accel_x_g = accel_x_raw / 16384.0
            accel_y_g = accel_y_raw / 16384.0
            accel_z_g = accel_z_raw / 16384.0

            # From datasheet: Temp in °C = (raw / 340) + 36.53
            temp_c = (temp_raw / 340.0) + 36.53

            gyro_x_dps = gyro_x_raw / 131.0
            gyro_y_dps = gyro_y_raw / 131.0
            gyro_z_dps = gyro_z_raw / 131.0

            records.append({
                "timestamp": ts,
                "accel_x_g": accel_x_g,
                "accel_y_g": accel_y_g,
                "accel_z_g": accel_z_g,
                "gyro_x_dps": gyro_x_dps,
                "gyro_y_dps": gyro_y_dps,
                "gyro_z_dps": gyro_z_dps,
                "temp_c": temp_c,
            })

            time.sleep(INTERVAL)

    df = pl.DataFrame(records)
    df.write_parquet(OUTPUT_FILE)
    print(f"Saved {len(records)} samples to {OUTPUT_FILE}")
    print(df.head())


if __name__ == "__main__":
    main()