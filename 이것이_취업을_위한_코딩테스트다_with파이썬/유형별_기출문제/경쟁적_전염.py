# 경쟁적 전염
# BFS로 풀게 되면, 입력 시간은 거의 무시해도 되고, 모든 칸 탐색 1회씩만 하고 끝, O(4만) 정도로 clear
from collections import deque

n, k = map(int, input().split()) # 시험관 한 변 길이 n, 바이러스는 1~k

board = []
virus_startLocations = [[] for _ in range(k+1)] # 각 바이러스 번호의 시작지점이 여기 저장되어 있음
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# 입력 받기
for i in range(n):
  row = list(map(int, input().split())) # 한 row 입력 받기
  for j in range(n): # row 탐색, 바이러스 시작 지점 좌표 파악해야 함
    if row[j] != 0: # 바이러스가 있는 경우
      virus_startLocations[row[j]].append((row[j], i, j, 0)) # (바이러스 번호, 행, 열, 시간) 저장
  board.append(row) # board도 채우기

s, x, y = map(int, input().split()) # s: 시간, x: 찾으려는 행 좌표, y: 찾으려는 열 좌표

# BFS 탐색하는 함수
def BFS():
  queue = deque()
  for locations in virus_startLocations: # 바이러스 번호 오름차순으로 좌표 queue에 집어 넣기
    for location in locations:
      queue.append(location)
  
  while queue: # queue가 빌 때까지
    v_num, now_y, now_x, time = queue.popleft() # queue에서 맨 왼쪽꺼 뽑기
    if time == s: # time이 s면, 이후에는 더 이상 퍼지면 안됨 (s초 시점에서의 위치를 확인하고 싶은 거니깐)
      continue # 걍 다음껄로 제낀다

    for i in range(4): # 사방 확인
      ny = now_y + dy[i]
      nx = now_x + dx[i]
      if ny < 0 or ny > n-1 or nx < 0 or nx > n-1: # 경계 벗어나면
        continue
      if board[ny][nx] != 0: # 이미 바이러스가 해당 칸에 퍼져있는 경우도
        continue
      board[ny][nx] = v_num # 해당 바이러스 번호 기입
      queue.append((v_num, ny, nx, time+1)) # (바이러스 번호, 행, 열, 시간) 저장

BFS() # BFS 수행해서, board에다가 다 입력
print(board[x-1][y-1]) # 출력한다 (없으면 0, 있으면 해당하는 바이러스 번호 나올거임)