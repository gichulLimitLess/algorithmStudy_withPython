# 낚시왕
# 격자판 크기 r, c / 상어 수 m
# r, c, m = map(int, input().split())
# f_board = [[0 for _ in range(c)] for _ in range(r)] # 물고기 "크기"만 저장할 f_board
# shark_infos = {}
# fishing_king_col = -1 # 낚시왕 초기 위치는 -1
# size_sum = 0 # 낚시왕이 잡은 상어 크기의 총합
# dy = [-1, 1, 0, 0]
# dx = [0, 0, 1, -1]
#
# # 같은 곳에 있는 애들은 소멸 처리해야 함 -> 그러고 f_board에 기록
# def check_shark():
#     loc = {} # 위치(y,x)를 key로, 상어 번호를 val로(-> 배열로 관리, 오름차순 정렬 후 맨 뒤에 꺼 빼고는 다 소멸처리)
#     for shark in shark_infos:
#         y, x = shark_infos[shark][0], shark_infos[shark][1]
#         if (y, x) in loc: # 이미 loc에 있다면
#             loc[(y,x)].append(shark)
#         else: # 없다면
#             loc[(y,x)] = [shark]
#
#     for location in loc: # loc을 탐색한다 -> value 값으로 길이가 1 초과라면, 거기서 가장 큰 애 빼고 다 날려야 한다
#         if len(loc[location]) > 1: # 여러 마리 상어가 있다면, 가장 큰 애 빼고 날려야 함
#             loc[location].sort()
#             for i in range(len(loc[location])-1): # 맨 마지막 애(가장 큰 상어) 빼고 다 shark_infos에서 정보 소멸
#                 del shark_infos[loc[location][i]]
#
#     for shark in shark_infos: # 삭제된 후, shark_infos 다시 돌아보며, 업데이트 된 정보로 f_board에 재 기록
#         y, x = shark_infos[shark][0], shark_infos[shark][1]
#         f_board[y][x] = shark # f_board에는 '크기'만 기록
#
# # 상어 이동하는 함수
# def moving_shark():
#     '''
#     (동시에 한 번에 움직임. 고려해야 할 것은 2가지)
#     1. 해당 이동 시 격자판의 경계를 넘었을 때, 반대로 방향을 돌리고 이동을 이어가야 함
#     2. 한 칸에 여러 상어 왔을 때, 가장 큰 애 빼고 모두 소멸 시켜야 한다
#     '''
#     for shark in shark_infos:
#         y, x, s, d = shark_infos[shark] # y, x, 속도, 방향 값 추출
#         f_board[y][x] = 0 # 우선 이동 전에, 원래 있던 자리를 비운다
#         # 경계를 넘어가는 것에 대해 한 번에 계산하기 위해 절댓값을 씌운다 (음수가 나올수도 있어서 해당 건에 대한 보정값임)
#         ny = abs(y+(dy[d]*s))
#         nx = abs(x+(dx[d]*s))
#         # =============== y축 기준 움직이는 애들 대상 ==============
#         if ny != y: # "움직인 애들" 대상으로만 해야 함
#             offset = 0
#             if y+(dy[d]*s) < 0: # 얘가 음수라면
#                 offset = 1
#             if ((ny // (r-1))+offset) % 2 == 0: # 이 값이 짝수인 경우 --> 방향이 바뀌면 안된다
#                 ny = ny % (r - 1) if d == 1 else (r - 1) - (ny % (r - 1))  # 좌표 상에서 실제 위치는 여기, 방향 값은 같다
#             elif ((ny // (r-1))+offset) % 2 == 1: # 이 값이 홀수인 경우 --> 방향이 바뀌어야 한다
#                 d = 0 if d == 1 else 1  # 방향 반대로 바꾼다
#                 ny = ny % (r-1) if d == 1 else (r-1)-(ny % (r-1)) # 좌표 상에서 실제 위치는 여기, 방향 값은 같다
#
#         # =============== x축 기준 움직이는 애들 대상 ==============
#         if nx != x: # "움직인 애들" 대상으로만 해야 함
#             offset = 0
#             if x + (dx[d] * s) < 0:  # 얘가 음수라면
#                 offset = 1
#             if ((s // (c - 1))+offset) % 2 == 0: # 이 값이 짝수인 경우 --> 방향이 바뀌면 안된다
#                 nx = nx % (c - 1) if d == 2 else (c - 1) - (nx % (c - 1))  # 좌표 상에서 실제 위치는 여기, 방향 값은 같다
#             elif ((s // (c-1))+offset) % 2 == 1: # 이 값이 홀수인 경우 --> 방향이 바뀌어야 한다
#                 d = 2 if d == 3 else 3 # 방향 반대로 바꾼다
#                 nx = nx % (c - 1) if d == 2 else (c - 1) - (nx % (c - 1))  # 좌표 상에서 실제 위치는 여기, 방향 값은 같다
#
#         # 정보 갱신
#         shark_infos[shark] = (ny, nx, s, d)
#
#     # 본격적으로 f_board에 이동 후 정보를 찍기 전에, 같은 곳에 겹쳐있는 애들 삭제해야 한다
#     # 그러고, f_board에 기록까지 하는 check_shark
#     check_shark()
#
# if m == 0: # 상어가 0마리이면, 애초에 잡을 수가 없잖아
#     print(0)
# else:
#     for _ in range(m): # 상어 정보 입력 받기
#         # 상어 위치 (r,c) / 속력 s / 이동 방향 d / 크기 z
#         y, x, s, d, z = map(int, input().split())
#         f_board[y-1][x-1] = z
#         shark_infos[z] = (y-1, x-1, s, d-1)
#
#     # 낚시왕이 격자판의 가장 오른쪽으로 이동을 끝마칠 때까지 반복
#     while fishing_king_col <= c-1:
#         fishing_king_col += 1 # 낚시왕 오른쪽으로 한 칸 이동
#         if fishing_king_col >= c: # 바깥으로 벗어났으면
#             break # 더 이상 상어를 잡을 수 없으니, 벗어난다
#         print(f_board)
#         for i in range(len(f_board)): # 낚시왕 있는 col에서, 위에서부터 아래로 탐색
#             if f_board[i][fishing_king_col] != 0: # 상어 있는 곳 최초 발견
#                 size_sum += f_board[i][fishing_king_col] # 크기 더하기 (-> 상어 잡아버림!)
#                 del shark_infos[f_board[i][fishing_king_col]] # 이 친구는 "상어 정보"에서 삭제한다
#                 f_board[i][fishing_king_col] = 0 # '빈 곳'으로 초기화
#                 break # 제일 가까운 상어'만' 잡으면 끝
#         # 상어 이동
#         moving_shark()
#
#     print(size_sum) # 낚시왕이 잡은 상어 크기의 총합 출력

'''
    위는 오답 풀이
    아래가 GPT와 함께한 효율적인 정답 풀이
'''
# =========================================================
# 🎣 낚시왕 (좌표 중심 상태 관리 Ver.)
# =========================================================

r, c, m = map(int, input().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

# 상어 정보: {(y, x): (s, d, z)}
shark_infos = {}
for _ in range(m):
    y, x, s, d, z = map(int, input().split())
    shark_infos[(y - 1, x - 1)] = (s, d - 1, z)

size_sum = 0


def catch_shark(col):
    global size_sum
    # 제일 위 상어 찾기
    for row in range(r):
        if (row, col) in shark_infos:
            s, d, z = shark_infos.pop((row, col))
            size_sum += z
            return


def move_sharks():
    global shark_infos
    new_sharks = {}

    for (y, x), (s, d, z) in shark_infos.items():
        # 속도 최적화 --> "반복"되는 구조가 있으니까요
        if d in [0, 1]:
            s %= (r - 1) * 2
        else:
            s %= (c - 1) * 2

        for _ in range(s):
            ny, nx = y + dy[d], x + dx[d]
            if not (0 <= ny < r and 0 <= nx < c):
                if d == 0: d = 1
                elif d == 1: d = 0
                elif d == 2: d = 3
                else: d = 2
                ny, nx = y + dy[d], x + dx[d]
            y, x = ny, nx

        # 충돌 시 큰 상어만 남김
        if (y, x) in new_sharks:
            if z > new_sharks[(y, x)][2]:
                new_sharks[(y, x)] = (s, d, z)
        else:
            new_sharks[(y, x)] = (s, d, z)

    shark_infos = new_sharks


for fishing_king_col in range(c):
    catch_shark(fishing_king_col)
    move_sharks()

print(size_sum)