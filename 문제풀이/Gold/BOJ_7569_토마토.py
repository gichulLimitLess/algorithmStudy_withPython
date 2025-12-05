# 토마토
'''
    [사고과정]
    - 전형적인 BFS 문제 + 이동 방향이 6 방향으로(위/아래/동/서/남/북) 진행
'''
from collections import deque
# 높이 h, 세로 n, 가로 m
m, n, h = map(int, input().split())
board = []
q = deque()
answer = 0

for i in range(h):
    layer = []
    for j in range(n):
        row = list(map(int, input().split()))
        for k in range(m): # 초기 '익어있는' 토마토 위치 파악 후 큐에 넣고 시작한다
            if row[k] == 1:
                q.append((i, j, k, 0)) # (좌표, 걸린 시간) 표시
        layer.append(row)
    board.append(layer)

dy = [0, 0, 1, -1, 0, 0]
dx = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
# 탐색 진행 --> O(100*100*100)
while q:
    z, y, x, time = q.popleft()
    answer = time # 맨 마지막에 들어간 time 값이 answer
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m: # 유효 범위 내에서
            # 방문하려는 곳이 토마토 없는 곳이 아니고, 방문하지 않은 곳이어야 함
            if board[nz][ny][nx] == 0: # '안 익은 토마토'일 때만, '익는' 상태가 전파될 수 있음
                board[nz][ny][nx] = 1
                q.append((nz, ny, nx, time+1))

# 다시 board 뒤지면서 '0' (안 익은 토마토) 있나 확인 --> O(100만)
def check(ans):
    for layer in board:
        for row in layer:
            for e in row:
                if e == 0: # 안 익은 거 하나라도 발견
                    return -1
    return ans # 여기까지 왔으면, 모두 다 1 또는 -1인 거임 --> 모두 익음!

print(check(answer)) # 답 출력