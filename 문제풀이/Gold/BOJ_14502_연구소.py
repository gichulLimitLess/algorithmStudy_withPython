# 연구소
from itertools import combinations
from collections import deque
import copy

# 입력 받기
n, m = map(int, input().split()) # 세로 크기 n, 가로 크기 m
board = []
candidate = [] # 벽을 놓을 수 있는 후보 좌표들 저장하는 곳
virus = [] # 바이러스의 시작 지점을 저장한 리스트
for i in range(n):
  row = list(map(int, input().split()))
  board.append(row)
  # 벽(1)을 놓을 수 있는 후보군 뽑아내기
  for j in range(m):
    if row[j] == 0: # 여기는 벽을 추가로 세울 수 있는 후보군
      candidate.append((i, j)) # (y, x) 좌표 순으로 저장
    elif row[j] == 2: # 바이러스 시작지점을 발견하면
      virus.append((i, j))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_safeArea = 0

# BFS 수행하는 함수
def BFS(board):
  queue = deque()
  for element in virus: # BFS 탐색 시작지점은 virus의 각 시작지점으로 설정해야 함
    queue.append(element)
  
  while queue: # queue가 빌 때까지, 하나씩 꺼내면서 확인
    now_y, now_x = queue.popleft() # queue에서 빼내기
    for i in range(4):
      ny = now_y + dy[i]
      nx = now_x + dx[i]
      if ny < 0 or ny > n-1 or nx < 0 or nx > m-1: # 유효한 좌표가 아닌 경우
        continue
      elif board[ny][nx] != 1 and board[ny][nx] != 2: # 방문한 곳이 아니라면
        board[ny][nx] = 2 # 바이러스 방문 표시하고
        queue.append((ny, nx)) # queue에 삽입


for combi in combinations(candidate, 3): # 후보군 중에서 3개의 좌표를 뽑아, 그걸 바탕으로 BFS 수행
  board_copy = copy.deepcopy(board) # 원본 board에는 영향이 가지 않도록 deepcopy를 수행해야 함
  safe_area = 0 # 현재 뽑은 조합으로 벽을 세웠을 경우, 안전 영역이 얼마나 있는지 저장할 것임
  for y, x in combi: # '1'을 표시할 좌표값을 가지고, 실제로 마킹
    board_copy[y][x] = 1
  
  # BFS 수행
  BFS(board_copy)

  # BFS 수행 후 board_copy 검사, 남아있는 안전 영역 확인
  for row in board_copy:
    for element in row:
      if element == 0: # 바이러스가 퍼지지 않은 빈칸일 경우
        safe_area += 1

  max_safeArea = max(safe_area, max_safeArea) # max 함수 갱신

print(max_safeArea) # 최댓값 출력