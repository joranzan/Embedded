import smbus
from time import sleep

DEVICE_BUS = 1
DEVICE_ADDR = 0x76

bus = smbus.SMBus(DEVICE_BUS)

while True:
    # 0xD0 register 의 값을 1byte 읽어서 출력해라. -> 88 이 나올 예정
    a = bus.read_byte_data(DEVICE_ADDR, 0xD0)
    print(a)
    sleep(0.5)
