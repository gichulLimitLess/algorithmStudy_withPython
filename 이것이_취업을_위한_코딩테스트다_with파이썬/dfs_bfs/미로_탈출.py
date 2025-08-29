# 실전 문제 2 - 미로 탈출
# 4 <= N, M <= 200
from collections import deque # 삼성 코테에서 deque 써도 상관 X

N, M = map(int, input().split())
board = []

for _ in range(N): # 배열 입력 받기
  row = list(map(int, input()))
  board.append(row)

def bfs(): # bfs를 위한 함수
  dy = [0, 0, 1, -1]
  dx = [1, -1, 0, 0]

  queue = deque([(0, 0, 1)]) # BFS 탐색을 위한 queue
  board[0][0] = 0 # 맨 처음 체킹

  while queue: # Queue가 빌 때까지 레츠고 
    y, x, dist = queue.popleft()
    for i in range(4): # 사방 탐색
      ny = y + dy[i]
      nx = x + dx[i]
      if ny == N-1 and nx == M-1: # 목적지 도달?
        return dist + 1

      if ny <= -1 or ny >= N or nx <= -1 or nx >= M: # 경계 검사
        continue
      if board[ny][nx] == 0: # 괴물 있는 곳이라면
        continue
      queue.append((ny, nx, dist+1)) # 여기까지 왔으면 해당 칸은 방문해야 함
      board[ny][nx] = 0 # 해당 칸 방문 처리

answer = bfs() # 탐색하는 함수
print(answer) # 참고: bfs는 최소 거리를 보장하는 알고리즘 -> 시간 복잡도: O(N*M)

# 위와 같이 풀어도 되고, board에다가 탐색 하면서 거리를 각 칸마다 일일이 적어도 될 듯