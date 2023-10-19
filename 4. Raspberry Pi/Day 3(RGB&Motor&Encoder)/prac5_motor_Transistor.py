from gpiozero import PWMLED
from time import sleep

motor = PWMLED(14)

while True:
    motor.value = 0
    sleep(1)
    motor.value = 0.1
    sleep(1)
    motor.value = 0.5
    sleep(1)
    motor.value = 1
    sleep(1)
