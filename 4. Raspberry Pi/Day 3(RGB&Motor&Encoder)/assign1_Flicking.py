from gpiozero import LED
from time import sleep

led = LED(2)
time = 1.000
while time>=0.010:
    led.on()
    sleep(time)
    led.off()
    sleep(time)
    time /= 2
