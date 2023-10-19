from gpiozero import AngularServo
from gpiozero import PWMLED, Button
from time import sleep
from signal import pause

servo = AngularServo(14, min_angle=0, max_angle=90)

red = PWMLED(17)
green = PWMLED(27)

btn1 = Button(15)
btn2 = Button(18)

def gogo():
    servo.angle = 45
    green.value = 1
    sleep(0.5)
    green.value = 0

def notgo():
    
    servo.angle = 0
    red.value = 1
    sleep(0.5)
    red.value = 0


btn1.when_pressed = gogo
btn2.when_pressed = notgo

pause()
