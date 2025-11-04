# 레이저 통신
'''
    [사고 과정]
    - 전형적인 BFS 문제에서 약간 변형된 문제이다
    - 이 문제에서 궁극적으로 구해야 할 것은, '설치해야 할 거울 개수의 최소 개수'
        --> 이것을 BFS의 기준으로 삼고, 이걸 기준으로 board에 '방문 표시' 하는 거 어떻게 생각함?
        --> 먼저 특정 칸에 도착했는데, 방향 회전 횟수가 더 많은 경우가 있을 수 있음?
            따라서, 방문 표시를 '지금까지 설치했던 거울 개수'로 하고, 그것보다 적은 개수여야만 Queue에 집어넣고, 방문표시
        --> 최종적으로, 도착한 C에 적혀 있는 숫자가 '설치해야 할 거울 개수의 최소값'
'''
from collections import deque
INF = int(1e9)

# 진행하는 방향에 따라서, 거울을 설치했을 때 진행 가능한 방향 리스트 제공
# 문제 조건에서 주어진 벽은 '/', '\'만 사용 가능하기 때문에, 이러한 설정 필요(사방 탐색으로 접근하면 X)
def making_move(d):
    if d == 0: # '동쪽'으로 진행 중이라면
        return [d, 2, 3]
    elif d == 1: # '서쪽'으로 진행 중이라면
        return [d, 3, 2]
    elif d == 2: # '남쪽'으로 진행 중이라면
        return [d, 0, 1]
    else: # '북쪽'으로 진행 중이라면
        return [d, 1, 0]

w, h = map(int, input().split())
board = []
check_board = [[[INF for _ in range(4)] for _ in range(w)] for _ in range(h)] # '각 칸에 도달하기 위한 거울의 최소 개수'를 저장하기 위한 배열
two_points = []
for i in range(h):
    row = list(input())
    for j in range(w):
        if row[j] == 'C': # '레이저로 연결해야 하는 칸' 발견
            two_points.append((i, j))
    board.append(row)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
q = deque()

for i in range(4): # 저장된 two_points 정보 기준으로.. 사방으로 뻗어 나가는 거 우선 queue에 넣기
    q.append((two_points[0][0], two_points[0][1], i, 0)) # (y,x,방향,현재까지 설치한 거울 개수) 넣기
    check_board[0][0][i] = 0 # 방문 표시

while q:
    y, x, d, cnt = q.popleft()
    if two_points[1][0] == y and two_points[1][1] == x: # 목적지에 도달했다면
        continue # --> 해당 칸에서부터는 더 이상 사방 탐색 안해도 됨

    moving_list = making_move(d) # 현재 들어온 방향에 따라서, 가능한 진행 방향 리스트 설정
    for i in moving_list: # 진행 가능한 방향들 탐색
        ny = y + dy[i]
        nx = x + dx[i]
        n_cnt = cnt
        if d != i: # 현재 설정된 방향과 다른 방향을 탐색하려 하는 거면
            n_cnt += 1 # 설치한 거울 개수 +1

        # 경계 검사 & 새로 가려는 곳이 벽이 아니어야 함
        if 0 <= ny <= h-1 and 0 <= nx <= w-1 and board[ny][nx] != '*':
            if check_board[ny][nx][i] > n_cnt: # 기존에 기록된 수보다 작은 수만 기록되어야 함
                check_board[ny][nx][i] = n_cnt
                q.append((ny, nx, i, n_cnt))

print(min(check_board[two_points[1][0]][two_points[1][1]])) # 최종 결과 출력