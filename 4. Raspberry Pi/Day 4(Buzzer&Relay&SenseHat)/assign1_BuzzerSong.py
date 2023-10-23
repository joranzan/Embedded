from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

lst1 = [493.88, 440, 391.99, 493.88, 587.32]
lst2 = [493.88, 440, 391.99, 493.88, 440]
lst3 = [493.88, 440, 391.99, 440, 440, 391.99, 440, 391.99, 493.88, 391]


b = TonalBuzzer(14)

while True:
    for i in range(5):
        b.play(lst1[i])
        sleep(0.2)
    sleep(0.5)   
    for i in range(5):
        b.play(lst2[i])
        sleep(0.2)
    sleep(0.5)   
    for i in range(10):
        b.play(lst3[i])
        sleep(0.2)
    b.play(lst3[9])
    sleep(0.5) 
    b.stop()
    break
