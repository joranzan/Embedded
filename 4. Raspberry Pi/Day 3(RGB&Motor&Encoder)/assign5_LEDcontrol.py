from gpiozero import RotaryEncoder, PWMLED, Button
from signal import pause

rotor = RotaryEncoder(15,18, wrap=True, max_steps=180)
rotor.steps = -180

red = PWMLED(17)
green = PWMLED(27)
yellow = PWMLED(10)

btn = Button(23)
r_duty = 1/121
g_duty = 1/120
y_duty = 1/120

red.value = r_duty



def change_rot():
    print(rotor.steps)
    if rotor.steps>=-180 and rotor.steps<=-60:
        red.value = r_duty * (rotor.steps + 181)
    else:
        red.value = 0
    if rotor.steps>-60 and rotor.steps<=60 :
        green.value = g_duty * (rotor.steps + 60)
    else :
        green.value = 0
    if rotor.steps>60 and rotor.steps<=180:
        yellow.value = y_duty * (rotor.steps -60 )
    else:
        yellow.value = 0
        

def click_btn():
    red.value = 0
    green.value = 0
    yellow.value = 0


rotor.when_rotated = change_rot
btn.when_pressed = click_btn


pause()
