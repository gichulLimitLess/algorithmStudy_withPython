# 토마토
from collections import deque

m, n = map(int, input().split())
board = []

for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

q = deque()
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
total_tomatoes = 0
tomatoes = 0
total_time = 0
visited = set()

# 1. 우선, 익을 수 있는 토마토의 초기 위치 파악
for i in range(n):
    for j in range(m):
        if board[i][j] == 1: # 익은 토마토가 있다면
            q.append((i, j, 0)) # (y, x, 시간) 정보 주입
        total_tomatoes += 1 if board[i][j] != -1 else 0

# 2. 하나씩 빼면서, 다 채워간다
while q:
    y, x, time = q.popleft()
    tomatoes += 1
    total_time = max(time, total_time) # 시간을 계속 갱신해 준다
    for i in range(4): # 사방 탐색
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny > n-1 or nx < 0 or nx > m-1: # 경계 검사
            continue
        if board[ny][nx] == 0 and (ny,nx) not in visited: # 방문하지 않은 "토마토"여야만 넣는다
            visited.add((ny, nx))
            q.append((ny, nx, time + 1))

# 3. 현재까지 갱신해 온 값에 따라 정답을 출력한다
if tomatoes == total_tomatoes: # 모두 익었다면
    print(total_time)
else: # 모두 익지 못했다면
    print(-1)