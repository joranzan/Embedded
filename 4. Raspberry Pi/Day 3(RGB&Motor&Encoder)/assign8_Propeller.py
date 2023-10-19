from gpiozero import PWMLED, Button, LED
from time import sleep
from signal import pause

a = LED(5)
b = LED(6)
c = LED(13)
d = LED(19)
e = LED(26)
f = LED(16)
g = LED(20)
dp = LED(21)

led = PWMLED(2)
btn1 = Button(17)
btn2 = Button(27)
btn3 = Button(22)
motor = PWMLED(14)

fnd = [[a,b,c,d,e,f],
        [b,c],
        [a,b,g,e,d],
        [a,b,g,c,d],
        [b,c,f,g],
        [a,f,g,c,d],
        [a,f,g,e,c,d],
        [a,b,c,f],
        [a,b,c,d,e,f,g],
        [a,f,g,b,c,d],
        ]
list = [0.33, 0.66, 1]
speed = 0
state = 0

def Segment(num):
    for i in fnd[num+1]:
        i.on()


def SegmentOff(num):
    for i in fnd[num+1]:
        i.off()

def switch1():
    global state
    print(state)
    if state==0:
        return
    global speed
    SegmentOff(speed)
    speed += 1
    print(speed)
    if speed>2:
        speed = 2
    motor.value =list[speed]
    Segment(speed)
    sleep(0.5)

def switch2():
    global state
    print(state)
    if state==0:
        return
    global speed
    SegmentOff(speed)
    speed -= 1
    if speed<0:
        speed = 0
    motor.value = list[speed]
    Segment(speed)

def switch3():
    global speed
    global state
    print(state)
    if state==0:
        state=1
        speed = 0
        motor.value = list[speed]
        Segment(speed)
        led.value = 1
    else:
        state=0
        SegmentOff(speed)
        speed=0
        motor.value = 0
        led.value = 0
    sleep(0.5)

btn1.when_released = switch1
btn2.when_released = switch2
btn3.when_released = switch3

pause()
