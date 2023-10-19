from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=15, trigger=14)
while True:
    print(sensor.distance, 'm')
    sleep(0.1)
