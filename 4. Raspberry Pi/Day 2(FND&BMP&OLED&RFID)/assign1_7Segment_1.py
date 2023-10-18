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

num = input()

for i in range(len(num)):
    digit = num[i]
    for j in fnd[int(digit)]:
       j.on()

    sleep(0.5)

    for j in fnd[int(digit)]:
        j.off( )
