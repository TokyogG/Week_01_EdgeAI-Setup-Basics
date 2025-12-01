from gpiozero import LED
from time import sleep

led = LED(17)

print("Blinking LED...")
while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)

# from gpiozero import LED
# led = LED(17)
# led.on()
