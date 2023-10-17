from gpiozero import LED
from time import sleep

red = LED(14) #GPIO pin number
yellow = LED(15)
green = LED(18)


while True:
    red.on()
    yellow.on()
    green.on()

    sleep(0.5)
    red.off()
    yellow.off()
    green.off()
    sleep(0.5)
