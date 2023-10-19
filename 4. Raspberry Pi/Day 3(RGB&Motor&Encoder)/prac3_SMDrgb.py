from gpiozero import PWMLED
from time import sleep

R = PWMLED(15)
G = PWMLED(18)
B = PWMLED(14)

while True:
    for i in range(10):
        R.value = i / 10
        G.value = (1 - i / 10)
        B.value = i / 10
        sleep(0.1)
