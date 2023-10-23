from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    gyro = sense.get_gyroscope()
    x = gyro['pitch']
    y = gyro['roll']
    z = gyro['yaw']
    print(f"Gyro - X:{x}, Y:{y}, Z:{z}")
    sleep(0.1)
    
