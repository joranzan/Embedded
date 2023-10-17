from gpiozero import LED
from time import sleep

red = LED(14) #GPIO pin number
yellow = LED(15)
green = LED(18)

while True:
    cmd = int(input("INPUT>> "))

    if cmd==1:
        if red.value==1:
            red.off()
        else:
            red.on()

    elif cmd==2:
        if yellow.value==1:
            yellow.off()
        else:
            yellow.on()

    elif cmd==3:
        if green.value==1:
            green.off()
        else :
            green.on()
    else:
        break
