from gpiozero import AngularServo
from time import sleep

servo = AngularServo(14, min_angle=0, max_angle=90)

while True:
    for i in range(0,91,15):
        servo.angle = i
        sleep(0.5)
