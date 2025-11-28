# 쉬운 최단거리
'''
    목표지점('2')로부터 각 지점까지의 최단거리 모두 찍기
        --> BFS 과정을 board에 기록하고, 모두 출력해내라
    전형적인 BFS 문제라고 생각하면 됨
'''
from collections import deque

n, m = map(int, input().split()) # 가로 n / 세로 m
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

def bfs(i, j):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    q = deque()
    q.append((i, j, 0))
    visited = set() # 방문 기록하는 set
    visited.add((i, j)) # 최초 방문 기록

    while q:
        y, x, cost = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 경계를 벗어나지 않고, 방문하지 않은 칸일때만 방문
            if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in visited:
                if board[ny][nx] == 1: # (+ 갈 수 있는 땅(0)이어야 함)
                    visited.add((ny, nx)) # 방문 표시
                    board[ny][nx] = cost + 1 # board에다가 값 찍어내기
                    q.append((ny, nx, cost+1))

    # 갈수는 있는데 도달 못하면 -1 출력해줘야 함
    for i in range(n):
        for j in range(m):
            # 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치
            if (i, j) not in visited and board[i][j] == 1:
                board[i][j] = -1

def find():
    # 1. 목표지점(2) 탐색
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2: # '목표지점' 발견했으면
                # 2. 거기 기준으로 탐색, 거리를 board에다가 다 찍어내기
                bfs(i, j)
                board[i][j] = 0 # 시작점은 0으로
                return

find() # 수행
# 3. 결과 출력
for row in board:
    for e in row:
        print(e, end=' ')
    print()
