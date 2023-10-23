from sense_hat import SenseHat
from collections import deque

sense = SenseHat()

# 맵을 정의합니다
Map = [
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0, 0]
]

purple = (128, 0, 128)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

current_r = 0
current_c = 7
target_r = 7
target_c = 0

total_path = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS():

    Visited = [[(-1, -1) for _ in range(8)] for _ in range(8)]

    # 큐를 초기화하고 시작 위치를 추가합니다
    queue = deque()
    queue.append((current_r, current_c))
    Visited[current_r][current_c] = (-1, -1)

    while queue:
        nowRow, nowCol = queue.popleft()

        if nowRow == target_r and nowCol == target_c:
            # 목표 위치에 도달하면 경로를 표시합니다
            backRow, backCol = Visited[nowRow][nowCol]
            sense.set_pixel(nowRow, nowCol, red)
            while backRow != current_r or backCol != current_c:

                sense.set_pixel(backRow, backCol, green)
                backRow, backCol = Visited[backRow][backCol]

        for d in range(len(dr)):
            nextRow, nextCol = nowRow + dr[d], nowCol + dc[d]
            if nextRow < 0 or nextCol < 0 or nextRow >= 8 or nextCol >= 8:
                continue
            if Visited[nextRow][nextCol] != (-1, -1) or Map[nextRow][nextCol] == 1:
                continue
            Visited[nextRow][nextCol] = (nowRow, nowCol)
            queue.append((nextRow, nextCol))

def refresh():
    # LED 매트릭스 초기화
    for i in range(8):
        for j in range(8):
            if Map[i][j] == 1:
                sense.set_pixel(i, j, black)
            else:
                sense.set_pixel(i, j, white)


refresh()
sense.set_pixel(current_r, current_c, purple)
sense.set_pixel(target_r, target_c, red)

while True:
    temp_r = current_r
    temp_c = current_c

    event = sense.stick.wait_for_event()

    print("Joystick {} {}".format(event.action, event.direction))

    # 조이스틱 이벤트 처리
    if event.action == "pressed":
        if event.direction == "up":
            current_c = max(current_c - 1, 0)
        elif event.direction == "down":
            current_c = min(current_c + 1, 7)
        elif event.direction == "left":
            current_r = max(current_r - 1, 0)
        elif event.direction == "right":
            current_r = min(current_r + 1, 7)

    # 벽에 부딪혔을 경우 이전 위치로 되돌립니다
    if Map[current_r][current_c] == 1:
        current_r = temp_r
        current_c = temp_c
    else:
        sense.set_pixel(temp_r, temp_c, white)

    refresh()
    BFS()  # BFS로 경로 찾기
    sense.set_pixel(current_r, current_c, purple)
    
    print("Joystick {} {}".format(event.action, event.direction))


