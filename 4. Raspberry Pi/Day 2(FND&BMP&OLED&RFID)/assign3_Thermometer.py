import sys
import os
import logging
import time
import traceback
from waveshare_OLED import OLED_0in96
from PIL import Image, ImageDraw, ImageFont
logging.basicConfig(level=logging.DEBUG)
from bmp280 import BMP280
from smbus import SMBus
from time import sleep
from datetime import datetime

try:

    disp = OLED_0in96.OLED_0in96()
    logging.info("\r 0.96inch OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()

    image1 = Image.new("1", (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)

    font = ImageFont.load_default()

    bus = SMBus(1)
    bmp280 = BMP280(i2c_dev=bus)

    while True:
        image1 = Image.new("1", (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        temp = bmp280.get_temperature()
        now = datetime.now()
        h, m, s = now.hour, now.minute, now.second

        time = " " + str(h) + ":"  +str('{:02}'.format(m)) + ":" + str(s)

        print('{:05.3f}°C'.format(temp))
        draw.text((30,5), " Temperature", font=font, fill=0)
        draw.text((30,20), str(' {:05.3f}°C'.format(temp)), font = font, fill = 0)
        draw.text((30,35),' Time' ,font=font, fill=0)
        draw.text((30,50), time, font=font, fill=0)
        disp.ShowImage(disp.getbuffer(image1))
        sleep(1)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    OLED_0in96.config.module_exit()
    exit()


