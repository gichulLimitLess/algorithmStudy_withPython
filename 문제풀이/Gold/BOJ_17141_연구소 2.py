# 연구소 2
from itertools import combinations
from collections import deque

INF = int(1e9)

n, m = map(int, input().split())
board = []
virus_start_candidates = []
for i in range(n):
    row = list(input().split(' '))
    for j in range(n):
        if row[j] == '2': # 바이러스를 놓을 수 있는 칸이라면
            virus_start_candidates.append((i, j))
    board.append(row)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

answer = []
# 모든 칸 검사 수행
def check(now_board):
    for row in now_board:
        for e in row:
            if e == 0:  # 빈 칸이 하나라도 존재하면
                return -1
    return 0

def BFS():
    global answer
    # 바이러스 위치 후보를 조합으로 뽑고, 그것을 토대로 각기 다른 BFS 수행 --> O(252*(2500+2500+2500))
    for virus_start_list in combinations(virus_start_candidates, m):
        now_board = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] == '1':
                    now_board[i][j] = -1

        q = deque()
        # 바이러스 위치 하나씩 돌아가면서 시작지점으로 박기
        for v_y, v_x in virus_start_list:
            q.append((v_y, v_x, 0))
            now_board[v_y][v_x] = -1
        time = 0
        # BFS 수행
        while q:
            y, x, t = q.popleft()
            time = max(t, time)
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and now_board[ny][nx] != -1:
                    now_board[ny][nx] = -1
                    q.append((ny, nx, t+1))
        # 모든 칸에 적혀있는 걸린 시간 체크
        return_val = check(now_board)
        answer.append(return_val if return_val==-1 else time)

# BFS 수행하고, 결과 좀 볼래
BFS()
min_val = INF
for e in answer:
    if e != -1:
        min_val = min(min_val, e)
if min_val == INF:
    print(-1)
else:
    print(min_val)