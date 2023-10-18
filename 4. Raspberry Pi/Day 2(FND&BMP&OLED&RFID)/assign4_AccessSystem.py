from mfrc522 import SimpleMFRC522
from gpiozero import LED

from time import sleep

green = LED(2)
red = LED(14)

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
try:

    for _ in range(3):
        green.on()
        red.on()
        sleep(0.7)
        green.off()
        red.off()
        sleep(0.7)

    green.on()
    red.off()

    print("System Ready")

    cnt = 0

    for f in fnd[cnt]:
        f.on()

    while True:
        
        print('Access System >> Tag your Card!')
        id = SimpleMFRC522().read()[0]
            
        if id==84401522692 or id==277423070072:
            print("Access System >> Accessed Completely!")
            
            for f in fnd[cnt]:
                f.off()

            cnt+=1
            for f in fnd[cnt]:
                f.on()

            for _ in range(5):
                green.on()
                sleep(0.2)
                green.off()
                sleep(0.2)
        
        else:
            print("Access System >> ERROR(Accessed Denied)")
            print(f"Invalid ID")
            green.off()
            for _ in range(5):
                red.on()
                sleep(0.2)
                red.off()
                sleep(0.2)
            green.on()

        sleep(0.3)

except KeyboardInterrupt:
    for i in range(10):
        for j in fnd[i]:
            j.off()
    green.off()
    red.off()
    print("\nAccess System >> BYE BYE")
    exit()
