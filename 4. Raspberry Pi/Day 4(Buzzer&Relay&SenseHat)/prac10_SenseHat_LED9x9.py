from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

sense.set_pixel(0,0, red)
sense.set_pixel(0,7, green)
sense.set_pixel(7,0, blue)
sense.set_pixel(7,7, white)
