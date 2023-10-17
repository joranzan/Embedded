from gpiozero import LED
from time import sleep

a = LED(5)
b = LED(6)
c = LED(13)
d = LED(19)
e = LED(26)
f = LED(16)
g = LED(20)
dp = LED(21)

fnd = [a,b,c,d,e,f,g,dp]
for i in range(8):
    fnd[i].on()
    sleep(0.1)

while True:
    sleep(1)
