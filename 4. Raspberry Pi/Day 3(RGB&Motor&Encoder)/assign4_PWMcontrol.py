from gpiozero import LED
from gpiozero import Button
from time import sleep

led = LED(2)

btn1 = Button(17)
btn2 = Button(27)

T = 0.002
a = 0.5


def func1():
    global a
    a+=0.1

def func2():
    global a
    a-=0.1

while True:
    print(a)
    if a>0.9:
        a=0.9

    elif a<0.1:
        a=0.1


    duty1 = T * a
    duty2 = T * (1-a)
    led.on()
    sleep(duty1)
    led.off()
    sleep(duty2)

    btn1.when_released = func1
    btn2.when_released = func2

