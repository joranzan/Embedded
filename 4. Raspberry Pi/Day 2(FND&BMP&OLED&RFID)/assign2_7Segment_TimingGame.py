from gpiozero import LED
from time import sleep
from gpiozero import Button

a = LED(5)
b = LED(6)
c = LED(13)
d = LED(19)
e = LED(26)
f = LED(16)
g = LED(20)
dp = LED(21)

# lazer = LED()
led = LED(14)
btn = Button(15)


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

def twinkle():
    for i in range(3):
        led.on()
        sleep(0.3)
        led.off()
        sleep(0.3)

def gogo():
    for i in range(10):
        for j in fnd[i]:
            j.on()
        sleep(0.5)
        if btn.is_pressed and i==7 :
                twinkle()
        for j in fnd[i]:
            j.off()
        if btn.is_pressed and i==7 :
                twinkle()
    for i in range(9,-1,-1):
        for j in fnd[i]:
            j.on()
        sleep(0.5)
        if btn.is_pressed and i==7:
            twinkle()
        for j in fnd[i]:
            j.off()
        if btn.is_pressed and i==7 :
                twinkle()

while(1):
    gogo()

