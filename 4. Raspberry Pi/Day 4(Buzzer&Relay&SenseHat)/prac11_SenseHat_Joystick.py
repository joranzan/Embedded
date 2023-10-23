from sense_hat import SenseHat

sense = SenseHat()

while True:
    for event in sense.stick.get_events():
        print("Joystick {} {}".format(event.action, event.direction))
