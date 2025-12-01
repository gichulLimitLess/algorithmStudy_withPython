# ==============================
# 주사위 시뮬레이션 문제 - 템플릿
# ==============================

# 1) 입력
N, M, y, x, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 2) 주사위 초기화
dice = [0, 0, 0, 0, 0, 0]  # top, bottom, north, south, east, west


# 3) 회전 함수
def roll(dice, direction):
    t, b, n, s, e, w = dice
    if direction == 1:  # East
        return [w, e, n, s, t, b]
    elif direction == 2:  # West
        return [e, w, n, s, b, t]
    elif direction == 3:  # North
        return [s, n, t, b, e, w]
    elif direction == 4:  # South
        return [n, s, b, t, e, w]


# 4) 이동 함수
def move(y, x, direction):
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    ny, nx = y + dy[direction-1], x + dx[direction-1]

    if not (0 <= ny < N and 0 <= nx < M):
        return y, x, False
    return ny, nx, True


# 5) 시뮬레이션 시작
for d in commands:
    ny, nx, ok = move(y, x, d)
    if not ok:
        continue

    # 위치 갱신
    y, x = ny, nx

    # 주사위 회전
    dice = roll(dice, d)

    # 보드와 바닥면(bottom) 상호작용
    if board[y][x] == 0:
        board[y][x] = dice[1]
    else:
        dice[1] = board[y][x]
        board[y][x] = 0

    # top 출력
    print(dice[0])
