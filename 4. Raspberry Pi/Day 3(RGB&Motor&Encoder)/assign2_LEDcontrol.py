from gpiozero import PWMLED
from time import sleep

led = PWMLED(2)
led.value = 0.5
while True:
    cmd = int(input())

    if cmd==1 :
        led.value += 0.1

    elif cmd==2:
        led.value -= 0.1
    else:
        print("Error Invalid Command")

