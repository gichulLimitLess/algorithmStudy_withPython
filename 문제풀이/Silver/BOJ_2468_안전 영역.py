# 안전 영역
'''
    [사고과정]
    n은 1 이상 100 이하 / 높이 값도 1 이상 100 이하
    높이 값을 1부터 100까지 순회하면서, 각 상황에서 잠기지 않는 영역의 개수를 구하고, 그 중 '최대값'을 구하면 될 듯
    --> 각 상황마다 visited[]를 활용해야 할 것임
'''
from collections import deque

n = int(input())
board = []
max_height = -1
for _ in range(n):
    row = list(map(int, input().split(' ')))
    max_height = max(row)
    board.append(row)

# 시작점을 기준으로 물에 잠기지 않은 부분 탐색
def bfs(s_y, s_x, visited, h):
    q = deque()
    q.append((s_y, s_x))
    visited.add((s_y, s_x))

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and (ny, nx) not in visited and board[ny][nx] > h:
                visited.add((ny, nx))
                q.append((ny, nx))

max_safeArea = -1
# board에 있는 최대 높이까지 돌아가보며 안전 영역의 개수를 센다 --> O(100 * 100 * 100)
# --> height는.. 해당 height 이하는 다 물에 잠겨있다는 뜻임
for height in range(0, max_height+1):
    visited = set()
    area_cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > height and (i, j) not in visited: # 탐색해야 할 곳이면
                bfs(i, j, visited, height)
                area_cnt += 1 # 영역 개수 +1
    max_safeArea = max(area_cnt, max_safeArea) # 최댓값 갱신

print(max_safeArea) # 장마철에 물에 안 잠기는 안전한 영역의 최대 개수