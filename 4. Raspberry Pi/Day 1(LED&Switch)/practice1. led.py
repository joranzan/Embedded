from gpiozero import LED
from time import sleep

red = LED(14) #GPIO pin number

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
