# 헌내기는 친구가 필요해
'''
    익숙한 BFS의 맛
'''
from collections import deque

n, m = map(int, input().split())
campus = []
for i in range(n):
    row = list(input())
    campus.append(row)

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
p_cnt = 0 # 만난 사람 수
visited = set() # 칸 방문 처리

# 도연이 위치 찾아서 시작 지점에 넣기
q = deque()
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            q.append((i, j))
            visited.add((i, j))
            break

while q:
    y, x = q.popleft()
    if campus[y][x] == 'P': # 사람 만났으면
        p_cnt += 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            # 방문하지 않은 칸이어야 하고, 해당 칸이 벽이 아니어야 함
            if (ny, nx) not in visited and campus[ny][nx] != 'X':
                visited.add((ny, nx))
                q.append((ny, nx))

# 결과 출력
if p_cnt == 0:
    print('TT')
else:
    print(p_cnt)