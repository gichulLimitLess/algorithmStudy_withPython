# # 온풍기 안녕!
# # ========== 1. 입력 받기 ==========
# # 조사하는 모든 칸의 온도가 k 이상이 되었는지 검사
# r, c, k = map(int, input().split())
# # 방의 기본 정보와 방의 "온도" 정보는 서로 오염되면 안되므로 따로 관리
# room = [] # 방 정보
# room_temp = [] # 방의 "온도" 정보
# '''
#     room의 각 칸에 있는 정보는 아래의 내용들 중 하나
#     - 0: 빈칸
#     - 1: 방향이 "오른쪽"인 온풍기가 있음
#     - 2: 방향이 "왼쪽"인 온풍기가 있음
#     - 3: 방향이 "위쪽"인 온풍기가 있음
#     - 4: 방향이 "아래"인 온풍기가 있음
#     - 5: 온도를 조사해야 하는 칸
# '''
# for _ in range(r):
#     row = list(map(int, input().split()))
#     room.append(row)
#
# # 벽 정보 입력 받기, 벽 개수 w
# wall_info = set()
# w = int(input())
# for _ in range(w):
#     y, x, t = map(int, input().split())
#     # 벽 정보 입력 받기 --> 나중에 가져다 사용하기 편하도록 set의 값은 "좌표 + 벽 위치"로!
#     wall_info.add((y, x, t))
#
# # "오 -> 왼 -> 위 -> 아래" 순으로 진행토록 함
# dy = [0, 0, -1, 1]
# dx = [1, -1, 0, 0]
#
# # print(wall_info)
#
#
# # ========== 2. 집에 있는 온풍기에서 바람 한 번 나옴 ==========
# # 업데이트 전에, 해당 칸으로 바람이 올 수 있는지부터 검사 --> "벽 검사" 해야 함
# def no_wall(y, x):
#     # 자기 "왼쪽"에 벽이 있다면 --> 왼쪽 위, 왼쪽, 왼쪽 아래에서 모두 접근 불가
#     if x-1 > 0 and (y, x-1, 1) in wall_info:
#         return False
#     # 자기 "왼쪽"엔 벽이 없는데, "자기 왼쪽 아래 칸"에 윗 방향으로 벽이 있는 경우 --> 바람 접근 못함
#     elif y+1 < r-1 and (y+1, x-1, 0) in wall_info:
#         return False
#     # 이외의 경우에는 바람 접근 가능
#     return True
#
# # 방의 "온도"를 업데이트 하는 함수
# # --> (y,x)는 시작 좌표, d는 방향
# def update_temp_board(y, x, d):
#     n_temp = 5 # 최초 온도는 5
#     cnt = 0
#     while n_temp > 0: # 온도가 0 초과일 때만 반복
#         y = y + dy[d]
#         x = x + dx[d]
#         if d == 0 or d == 1: # 방향이 오른쪽(0) 혹은 왼쪽(1)인 경우
#             for i in range(y-cnt, y+cnt+1):
#                 if 0 < i < r-1 and no_wall(i, x): # 유효 범위 안에 있을때만, 그리고 바람이 닿을 수 있을때만
#                     room_temp[i][x] += n_temp
#         elif d == 2 or d == 3: # 방향이 위쪽(2) 혹은 아래쪽(3)인 경우
#             for i in range(x-cnt, x+cnt+1):
#                 if 0 < i < c-1 and no_wall()
#         n_temp -= 1 # 온도 1도 낮춘다
#         cnt += 1 # 온도 찍히는 범위를 늘린다
#
# def blow_wind():
#     for i in range(r):
#         for j in range(c):
#             # 온풍기가 있는 칸이라면
#             if 1 <= room[i][j] <= 4:
#                 update_temp_board(i, j, room[i][j]-1)

'''
    [오답노트]
    --> 시뮬레이션은 제발.. 완벽주의로 가지 말고, "우선 그것이 비효율적인 것 같아도 시도해 보는 거다"
'''

from collections import deque
R, C, K = map(int, input().strip().split())
room = [list(map(int, input().strip().split())) for _ in range(R)]
W = int(input())
wall = []
for _ in range(W):
    x, y, t = map(int, input().strip().split())
    wall.append((x-1, y-1, t))
warm = [[0]*C for _ in range(R)]

def can_go(h_num, dirx, diry, x, y):
    go = True
    if h_num == 1: # 오
        if (dirx, diry) == (-1, 1) and ((x, y, 0) in wall or (x-1, y, 1) in wall): go = False
        elif (dirx, diry) == (0, 1) and (x, y, 1) in wall: go = False
        elif (dirx, diry) == (1, 1) and ((x+1, y, 0) in wall or (x+1, y, 1) in wall): go = False
    elif h_num == 2: # 왼
        if (dirx, diry) == (-1, -1) and ((x, y, 0) in wall or (x-1, y-1, 1) in wall): go = False
        elif (dirx, diry) == (0, -1) and (x, y-1, 1) in wall: go = False
        elif (dirx, diry) == (1, -1) and ((x+1, y, 0) in wall or (x+1, y-1, 1) in wall): go = False
    elif h_num == 3: # 위
        if (dirx, diry) == (-1, -1) and ((x, y-1, 0) in wall or (x, y-1, 1) in wall): go = False
        elif (dirx, diry) == (-1, 0) and (x, y, 0) in wall: go = False
        elif (dirx, diry) == (-1, 1) and ((x, y+1, 0) in wall or (x, y, 1) in wall): go = False
    elif h_num == 4: # 아래
        if (dirx, diry) == (1, -1) and ((x+1, y-1, 0) in wall or (x, y-1, 1) in wall): go = False
        elif (dirx, diry) == (1, 0) and (x+1, y, 0) in wall: go = False
        elif (dirx, diry) == (1, 1) and ((x+1, y+1, 0) in wall or (x, y, 1) in wall): go = False
    return go

def bfs(dx, dy, x, y, h_num):
    check = [[0]*C for _ in range(R)]
    q = deque()
    nx, ny = 0, 0
    if h_num == 1: nx, ny = x, y+1
    elif h_num == 2: nx, ny = x, y-1
    elif h_num == 3: nx, ny = x-1, y
    elif h_num == 4: nx, ny = x+1, y
    check[nx][ny] = 5
    q.append(((nx, ny)))
    while q:
        x, y = q.popleft()
        for i in range(3):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < R and 0 <= ny < C and not check[nx][ny] and check[x][y] - 1 > 0 and can_go(h_num, dx[i], dy[i], x, y):
                check[nx][ny] = check[x][y] - 1
                q.append((nx, ny))
    return check

def heaters():
    for r in range(R):
        for c in range(C):
            if 0 < room[r][c] < 5: # 온풍기인 경우
                check = None
                if room[r][c] == 1:
                    check = bfs([-1, 0, 1], [1, 1, 1], r, c, 1)
                elif room[r][c] == 2:
                    check = bfs([-1, 0, 1], [-1, -1, -1], r, c, 2)
                elif room[r][c] == 3:
                    check = bfs([-1, -1, -1], [-1, 0, 1], r, c, 3)
                elif room[r][c] == 4:
                    check = bfs([1, 1, 1], [-1, 0, 1], r, c, 4)

                for i in range(R):
                    for j in range(C):
                        warm[i][j] += check[i][j]

def change_temp():
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    change_warm = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<R and 0<=ny<C:
                    if (dx[k], dy[k]) == (0, 1) and (i, j, 1) in wall: continue
                    elif (dx[k], dy[k]) == (0, -1) and (i, j-1, 1) in wall: continue
                    elif (dx[k], dy[k]) == (-1, 0) and (i, j, 0) in wall: continue
                    elif (dx[k], dy[k]) == (1, 0) and (i+1, j, 0) in wall: continue
                    if warm[i][j] > warm[nx][ny]:
                        ch = (warm[i][j] - warm[nx][ny]) // 4
                        change_warm[i][j] -= ch
                        change_warm[nx][ny] += ch
    for i in range(R):
        for j in range(C):
            warm[i][j] += change_warm[i][j]

def down_temp():
    for i in range(R):
        for j in range(C):
            if i == 0 or j == 0 or i == R-1 or j == C-1:
                if warm[i][j]:
                    warm[i][j] -= 1

def check_to_stop():
    flag = True
    for i in range(R):
        for j in range(C):
            if room[i][j] == 5 and warm[i][j] < K:
                flag = False
                break
    return flag

ans = 0
while True:
    if ans > 100:
        break
    heaters()
    change_temp()
    ans += 1
    down_temp()
    if check_to_stop():
        break
print(ans)

'''
    ======== 앞으로 시뮬레이션 문제 풀 때 사고 루프 ========
    1. 현상 분리 (무엇이 일어나는가)
    2. 상태 분리 (어디에 저장되는가 --> 무슨 자료구조 쓸지.. 어떻게 상태 저장할 것인지..)
    3. 순서 정의 (언제 일어나는가 --> 동시에 처리되고 이러는 거.. 잘 고려해라)
    4. 조건 해석 (어떻게 제한되는가)
'''

# 출처: https://jjujju31.tistory.com/80 [현재를 가치있게 쓰자:티스토리]