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


from sense_hat import SenseHat

sense = SenseHat()




green = (0, 255, 0)
black = (1, 1, 1)
white = (255, 255, 255)


target_r = 7
target_c = 0

Visited = [[0] * 8 for _ in range(8)]
total_path = []
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def DFS(nowRow, nowCol, path):
    global target_r, target_c
    global total_path
    global dr, dc
    global Visited
    if target_r==nowRow and target_c==nowCol:
        total_path.append(path)
        return
    
    for d in range(len(dr)):
        nextRow, nextCol = nowRow + dr[d], nowCol + dc[d]
        if nextRow<0 or nextCol<0 or nextRow>=8 or nextCol>=8:
            continue
        if Visited[nextRow][nextCol]==1 or Map[nextRow][nextCol]==1: 
            continue;
        Visited[nextRow][nextCol] = 1
        DFS(nextRow, nextCol, path+[(nextRow,nextCol)])
        Visited[nextRow][nextCol] = 0



def ShowPath(num):
    global total_path
    for i in total_path[num]:
        row, col = i
        sense.set_pixel(row, col, green)


def refresh():
    for i in range(8):
        for j in range(8):
            if Map[i][j]==1:
                sense.set_pixel(i,j,black)
            elif Map[i][j]==0:
                sense.set_pixel(i,j,white)


Visited[0][7]=1
DFS(0,7,[(0,7)])
refresh()
index = 0




while True:
    event = sense.stick.wait_for_event()
    

    print("Joystick {} {}".format(event.action, event.direction))
    
    event = sense.stick.wait_for_event()
    refresh()
    print("Joystick {} {}".format(event.action, event.direction))
    
    ShowPath(index)
    index += 1
    if index>=len(total_path):
        index = 0



