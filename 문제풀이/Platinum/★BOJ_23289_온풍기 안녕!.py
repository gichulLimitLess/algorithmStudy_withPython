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