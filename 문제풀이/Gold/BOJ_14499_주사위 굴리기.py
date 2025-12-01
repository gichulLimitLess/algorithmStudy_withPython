# 주사위 굴리기
'''
    [사고과정]
    - 전형적인 '시뮬레이션' 문제로 판단
    - 정확히 문제에서 주어진 조건들을 '구현'하자
'''
# 지도의 세로 크기 n, 가로 크기 m
# 주사위 놓은 곳의 좌표 x, y
# 명령 개수 k
# n, m, x, y, k = map(int, input().split())
# board = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     board.append(row)
# instructions = list(map(int, input().split())) # 이동하는 명령 (동: 1, 서: 2, 북: 3, 남: 4)
# now = [x, y] # 현재 주사위 위치 초기화
#
# # 주사위의 전개도를 아래와 같이 구성 (x방향/y방향)
# dice_x = [0, 0, 0, 0]
# dice_y = [0, 0, 0, 0]
#
# # 주사위를 '이동' 시키는 함수
# # --> 매개변수로 들어올 때, -1을 해서 들어올 예정
# def move(inst):
#     global dice_x, dice_y
#     dy = [0, 0, -1, 1]
#     dx = [1, -1, 0, 0]
#     ny = now[0] + dy[inst-1]
#     nx = now[1] + dx[inst-1]
#
#     # 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
#     # ---> 따라서, 경계를 벗어나지 않을때만 수행
#     if 0 <= ny < n and 0 <= nx < m:
#         # 우선 시작 전에, '현재 주사위 위치' 갱신
#         now[0] = ny
#         now[1] = nx
#         # 1. 각 방향에 대해서 주사위 이동 --> O(4)
#         if inst == 1: # '동쪽'으로 이동
#             dice_x = [dice_x[3]] + dice_x[:3]
#             dice_y[1] = dice_x[1]
#             dice_y[3] = dice_x[3]
#         elif inst == 2: # '서쪽'으로 이동
#             dice_x = dice_x[1:] + [dice_x[0]]
#             dice_y[1] = dice_x[1]
#             dice_y[3] = dice_x[3]
#         elif inst == 3: # '북쪽'으로 이동
#             dice_y = dice_y[1:] + [dice_y[0]]
#             dice_x[1] = dice_y[1]
#             dice_x[3] = dice_y[3]
#         elif inst == 4: # '남쪽'으로 이동
#             dice_y = [dice_y[3]] + dice_y[:3]
#             dice_x[1] = dice_y[1]
#             dice_x[3] = dice_y[3]
#
#         # 2. 이동한 곳의 board 상태에 따라 분기처리 --> O(1)
#         if board[ny][nx] == 0: # 이동한 칸에 적혀있는 수가 0인 경우
#             board[ny][nx] = dice_y[3] # 바닥에 있는 수가 board에 복사됨
#         else: # 이동한 칸에 적혀있는 수가 0이 아닌 경우
#             # 칸에 쓰여있는 수가 주사위의 바닥면으로 복사
#             dice_x[3] = board[ny][nx]
#             dice_y[3] = board[ny][nx]
#             # 칸에 쓰여 있는 수는 0이 된다
#             board[ny][nx] = 0
#
#         # 3. 주사위가 이동하고 나서 상단(dice_x[1] or dice_y[1])에 쓰여있는 값 출력
#         print(dice_x[1])
#
# for inst in instructions: # 명령 하나씩 수행 --> O(1000)
#     move(inst)

# ================= [주사위 굴리기 할 때 위처럼 풀면 안됨(우연히 맞긴 함) / 아래처럼 풀어보자] ======================

# 주사위 굴리기 - 기존 구조 유지 + 6면 패턴으로 수정된 정답 버전

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
instructions = list(map(int, input().split()))

# 현재 주사위 위치
now = [x, y]
dice = [0] * 6


def roll(inst):
    global dice
    t, b, n, s, e, w = dice[:]  # 반드시 복사

    if inst == 1:  # 동
        dice = [w, e, n, s, t, b]
    elif inst == 2:  # 서
        dice = [e, w, n, s, b, t]
    elif inst == 3:  # 북
        dice = [s, n, t, b, e, w]
    elif inst == 4:  # 남
        dice = [n, s, b, t, e, w]

    return dice


def move(inst):
    global now, dice

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    ny = now[0] + dy[inst - 1]
    nx = now[1] + dx[inst - 1]

    if not (0 <= ny < n and 0 <= nx < m):
        return

    now[0], now[1] = ny, nx
    roll(inst)

    if board[ny][nx] == 0:
        board[ny][nx] = dice[1]
    else:
        dice[1] = board[ny][nx]
        board[ny][nx] = 0

    print(dice[0])


for inst in instructions:
    move(inst)
