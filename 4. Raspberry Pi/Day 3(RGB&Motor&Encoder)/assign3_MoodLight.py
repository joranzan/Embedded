from gpiozero import Button
from gpiozero import PWMLED
from time import sleep

R = PWMLED(18)
G = PWMLED(15)
B = PWMLED(14)

btn1 = Button(17)
btn2 = Button(27)
btn3 = Button(22)

R.value = 0.5
G.value = 0.5
B.value = 0.5


while True:

    if btn1.is_pressed:
        value = R.value
        value += 0.1
        if(value>1.0):
            value = 0.0
        R.value = value

    elif btn2.is_pressed:
        value = G.value
        value += 0.1
        if(value>1.0):
            value = 0.0
        G.value = value

    elif btn3.is_pressed:
        value = B.value
        value += 0.1
        if(value>1.0):
            value = 0.0
        B.value = value

    else:
        continue
