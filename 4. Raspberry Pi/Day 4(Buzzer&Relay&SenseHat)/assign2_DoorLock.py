from gpiozero import AngularServo, LED, Button
from time import sleep

servo = AngularServo(14, min_angle=0, max_angle=90)
red = LED(2)
green = LED(3)
btn1 = Button(15)
btn2 = Button(18)

password = [1, 0, 0, 1]
press = []

def press1():
    press.append(1)
    print(1)
def press0():
    press.append(0)
    print(0)

while len(press) < 4:
        btn1.when_pressed = press1
        btn2.when_pressed = press0

while True:
  
    flag = 0    
    if len(press) == 4:
        for i in range(4):
            if (press[i] != password[i]):
                flag = 1

        if flag == 0:
            green.on()
            servo.angle = 90
            sleep(1)
            servo.angle = 0
            green.off()
    
        elif flag == 1:
            red.on()
            sleep(1)
            red.off()
       
        press.clear()
