# 나이트의 이동
'''
    전형적인 BFS 문제인데, 이동이 약간 특이한 부분
    --> 그것만 하면 별거 없는 문제임
'''
from collections import deque

tc = int(input())
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]
for _ in range(tc):
    l = int(input()) # 체스판의 한 변의 길이 l 입력 받기
    start_y, start_x = map(int, input().split())
    fin_y, fin_x = map(int, input().split())

    visited = set() # 방문 처리 위함
    q = deque()
    q.append((start_y, start_x, 0))
    visited.add((start_y, start_x))

    # 큐가 빌 때까지
    while q:
        now_y, now_x, cnt = q.popleft()
        if fin_y == now_y and fin_x == now_x: # 목적지에 도달 했으면
            print(cnt)
            break
        for i in range(8):
            ny = now_y + dy[i]
            nx = now_x + dx[i]
            if 0 <= ny <= l-1 and 0 <= nx <= l-1:
                if (ny, nx) not in visited: # 방문하지 않았을 때만
                    visited.add((ny, nx))
                    q.append((ny, nx, cnt+1))