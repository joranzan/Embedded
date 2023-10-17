from gpiozero import Button, LED
from time import sleep

red = LED(14)
yellow = LED(15)
green = LED(18)


btn1 = Button(23)
btn2 = Button(24)


while(True):

    if btn1.is_pressed:
        red.on()
        sleep(0.5)
        red.off()
        yellow.on()
        sleep(0.5)
        yellow.off()
        green.on()
        sleep(0.5)
        green.off()
    
    elif btn2.is_pressed:
        red.on()
        yellow.on()
        green.on()
        sleep(1)
        red.off()
        yellow.off()
        green.off()

    else: 
        continue
        


