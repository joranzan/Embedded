from bmp280 import BMP280
from smbus import SMBus
from time import sleep

bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

while True:
    temp = bmp280.get_temperature()
    pres = bmp280.get_pressure()
    print('{:05.2f}oC {:05.2f}hPa'.format(temp, pres))
    sleep(1)
