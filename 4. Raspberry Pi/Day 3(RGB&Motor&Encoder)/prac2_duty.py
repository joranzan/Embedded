from gpiozero import LED
from time import sleep

led = LED(3)

# T = 0.1
# f = 10Hz
# duty rate = 80%
while True:
    led.on()
    sleep(0.08)
    led.off()
    sleep(0.02)

