from sense_hat import SenseHat
from time import sleep


Map = [
        [0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,0],
        [0,1,0,0,0,1,0,0],
        [0,1,1,1,0,1,0,0],
        [0,0,0,0,0,1,1,0],
        [0,1,1,1,0,0,0,0]
]


sense = SenseHat()




yellow = (0, 255, 0)
black = (1, 1, 1)
white = (255, 255, 255)


cur_r = 4
cur_c = 3

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up():
    global cur_r
    cur_r = clamp(cur_r - 1)

def pushed_down():
    global cur_r
    cur_r = clamp(cur_r + 1)

def pushed_left():
    global cur_c
    cur_c = clamp(cur_c - 1)

def pushed_right():
    global cur_c
    cur_c = clamp(cur_c + 1)

def refresh():
    for i in range(8):
        for j in range(8):
            if Map[i][j]==1:
                sense.set_pixel(i,j,black)
            elif Map[i][j]==0:
                sense.set_pixel(i,j,white)

    sense.set_pixel(cur_r, cur_c, yellow)





while True:
    gyro = sense.get_gyroscope()
    x = gyro['pitch']
    y = gyro['roll']
    temp_r = cur_r
    temp_c = cur_c

    if y<330 and y>250:
        pushed_left()
        sleep(0.1)
    elif y>20 and y<180:
        pushed_right()
        sleep(0.1)
    if x>10 and x<90:
        pushed_up()
        sleep(0.1)
    elif x<330 and x>250:
        pushed_down()
        sleep(0.1)
    
    if Map[cur_r][cur_c]==1:
        cur_r = temp_r
        cur_c = temp_c
    else:
        sense.set_pixel(temp_r,temp_c,white)
    
    refresh()

    print(f"Gyro - X:{x}, Y:{y}")
    
