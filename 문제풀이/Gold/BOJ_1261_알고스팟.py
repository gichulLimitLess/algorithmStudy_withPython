# 알고스팟
'''
    [사고과정]
    - 기존의 격자 그래프 탐색 문제와 비슷하지만..
        중요한 차이점은.. 벽을 '최소'로만 깨 부셔야 한다
        즉, 무작정 기존의 BFS처럼 사방을 탐색하는 게 아니라는 것이다
        '다익스트라'의 냄새가 나는 것이다
    - '최소 힙'에다가 (현재까지 비용, y, x) 형태로 집어 넣으면 되는 거다
        그럼 '최소 힙'은 알아서 현재까지 비용이 '최소'인 경우를 쭉쭉 뽑아줄 것이다
'''
import heapq
INF = int(1e9)

m, n = map(int, input().split())
board = []
distance = [[INF for _ in range(m)] for _ in range(n)]
for _ in range(n):
    row = [int(e) for e in list(input())]
    board.append(row)

q = []
heapq.heappush(q, (0, 0, 0)) # (현재까지 비용, y, x) 넣고 시작
distance[0][0] = 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while q:
    dist, y, x = heapq.heappop(q)
    if distance[y][x] < dist: # 이미 더 작은 값이 저장되어 있다면
        continue
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m: # 범위 안에 있어야만 가능
            cost = dist + board[ny][nx]
            if distance[ny][nx] > cost: # 최소값을 갱신해야 할 때만
                distance[ny][nx] = cost
                heapq.heappush(q, (cost, ny, nx))

# 여기 저장되어 있는 값이 여기까지 오는 데 사용한 '최소 비용' == 부셔야 할 최소 벽 개수
print(distance[n-1][m-1])