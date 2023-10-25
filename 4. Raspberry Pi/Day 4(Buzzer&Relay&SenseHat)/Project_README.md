# Sense Hat 프로젝트 

### 1) 기울일 때 LED 점의 위치 변경

- IMU 다양한 센서 중 하나
  
- 맵 밖으로 나가지 않는다
  
- 지도 추가
  
- 지도를 밟을 수 없음 (벽 통과 금지)
  
<br>

------------------------------------------------


### 2) 모든 경로 출력

- 출발지점 : (0,0)
  
- 도착지점 : (7,7)
  
- 모두 같은 맵
  
- 버튼을 누를 때 마다 경로 출력됨 (모든 경로)
  
- 3개의 경로가 있다면 1->2->3->1->2->3 반복

<br>

---------------------------------------------
### 3) 기울여서 LED점 이동시킴

- 현재 LED점의 위치에 도착지점까지의 최단 경로가 표시
  
- 실시간 출력
  
- BFS DFS 암거나
  