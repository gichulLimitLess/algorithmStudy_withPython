# 화성 탐사
# 각 칸에 비용이 저장되어 있음 -> 값을 누적해 가는 dp 문제 각

# tc = int(input())
# res = []
# for _ in range(tc): # 테케 수만큼 반복
#     n = int(input())
#     board = []
#     for _ in range(n): # board 채우기
#         row = list(map(int, input().split()))
#         board.append(row)
#
#     # 1. dp 문제로 접근해야 하니, 초기값 세팅
#     for i in range(1, n):
#         board[0][i] += board[0][i-1]
#         board[i][0] += board[i-1][0]
#
#     # 2. board에 최소 경로에 대해, 값을 누적해 더해간다
#     # board[i][j] -> (i, j)까지 오는 데 최소 비용
#     for i in range(1, n):
#         for j in range(1, n):
#             board[i][j] = min(board[i-1][j], board[i][j-1]) + board[i][j]
#
#     print(board)
#     res.append(board[n-1][n-1]) # (n-1, n-1)의 위치로 이동하는 최소 비용 출력
#
# for e in res: # 정답 한 줄에 하나씩 출력
#     print(e)

# 정답 코드는 아래에
from heapq import heappush, heappop

tc = int(input())

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(tc):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)] # 그래프를 '인접' 행렬로 사용했음
    dist = [[INF]*n for _ in range(n)]

    q = []
    heappush(q, (graph[0][0], 0, 0))
    dist[0][0] = graph[0][0]

    while q:
        cost, x, y = heappop(q)
        if dist[x][y] < cost:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heappush(q, (new_cost, nx, ny))

    print(dist[n-1][n-1])


'''
    [오답노트]
    - 뭔가 경로 누적을 한다는 느낌만 받고, DP를 썼다가 틀렸다.
        -> "상하좌우" 모두로 움직일 수 있다. 이런 경우에는 DP를 쓰면 안된다
        -> DP는 이동 방향이 단방향(오른쪽/아래 등)일 때만 사용 가능하다!
        (이동 방향이 제한되어 있지 않다면, 그리고 가중치가 모두 다르다면, 최단 경로는 Dijkstra로 풀어야 한다)
'''