from gpiozero import Button

btn = Button(15)

while True:
    if btn.is_pressed:
        print('ON')
    else:
        print('OFF')
