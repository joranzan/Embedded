from gpiozero import LED
from time import sleep

lazer = LED(23) #GPIO pin number

while True:
    lazer.on()
    sleep(1)
    lazer.off()
    sleep(1)
