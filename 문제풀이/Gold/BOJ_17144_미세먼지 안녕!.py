# 미세먼지 안녕!
'''
    [사고과정]
    - 이전에 풀었던 '온풍기 안녕!'의 조금 쉬운 버전
    --> 차분하게 구현하라는 대로 구현하면 되는 '시뮬레이션' 문제
    - 주요 액션은 2가지,
        1) 미세먼지 확산
        2) 공기청정기 작동
'''
import copy

r, c, t = map(int, input().split())
board = []
cleaner_loc = -1
for i in range(r):
    row = list(map(int, input().split()))
    if row[0] == -1 and cleaner_loc == -1: # 공기청정기 있는 위치라면
        cleaner_loc = i
    board.append(row)

# 미세먼지 확산 --> O(2500 + 2500)
def dust_spread():
    c_board = copy.deepcopy(board) # 모든 미세먼지가 '동시에' 퍼지기 때문에, 상태 오염되면 안됨
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    # 보드 탐색
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0: # board에 적혀있는 수가 0보다 큰 경우 == 미세먼지 있는 칸인 경우
                s_dust = board[i][j] // 5 # 흩뿌려질 미세먼지 양 (미리 계산해 두어야 함)
                for k in range(4): # 사방 탐색하면서 진행
                    ny = i + dy[k]
                    nx = j + dx[k]
                    # 인접한 방향에 공기청정기가 있거나, 칸이 없을때는 확신 시키면 안됨 --> 그 외엔 무조건 ok
                    if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != -1:
                        c_board[ny][nx] += s_dust
                        c_board[i][j] -= s_dust
    return c_board

# 공기청정기 작동 ('위쪽' 부분) ==> '반시계방향'으로 회전 --> O(200)
def blow_wind_upper():
    # 공기청정기 '위쪽' 좌표 저장
    nowY = cleaner_loc
    nowX = 0
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    dir = 0
    prev = 0
    while True:
        # 공기청정기 윗부분의 바로 윗쪽에 도착했을 때
        if nowY == cleaner_loc-1 and nowX == 0:
            break
        ny = nowY + dy[dir]
        nx = nowX + dx[dir]
        if 0 <= ny < r and 0 <= nx < c: # 그 방향으로 전진 가능할 때만..
            temp = board[ny][nx]
            board[ny][nx] = prev
            prev = temp
            # 좌표도 밀어준다
            nowY = ny
            nowX = nx
        else: # 전진이 안된다면.. 그냥 방향만 바꿔주고 다시 살펴봐야 한다
            dir += 1

# 공기청정기 작동 ('아래쪽' 부분) ==> '시계방향'으로 회전 --> O(200)
def blow_wind_lower():
    # 공기청정기 '아래쪽' 좌표 저장
    nowY = cleaner_loc+1
    nowX = 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    dir = 0
    prev = 0
    while True:
        # 공기청정기 윗부분의 바로 윗쪽에 도착했을 때
        if nowY == cleaner_loc + 2 and nowX == 0:
            break
        ny = nowY + dy[dir]
        nx = nowX + dx[dir]
        if 0 <= ny < r and 0 <= nx < c:  # 그 방향으로 전진 가능할 때만..
            temp = board[ny][nx]
            board[ny][nx] = prev
            prev = temp
            # 좌표도 밀어준다
            nowY = ny
            nowX = nx
        else:  # 전진이 안된다면.. 그냥 방향만 바꿔주고 다시 살펴봐야 한다
            dir += 1

# t초 동안 동작 시뮬레이션 --> O(1000 * (5000+400))
for _ in range(t):
    board = dust_spread() # 1. 미세먼지 확산 --> O(5000)
    # 2. 공기청정기 작동 (-> 위/아래는 각각 '반시계', '시계' 방향으로 바람 회전) --> O(200+200)
    blow_wind_upper()
    blow_wind_lower()

# t초 후에 남아있는 미세먼지 양 구해서 출력
total = 0
for row in board:
    for e in row:
        if e > 0: # 미세먼지가 남아 있다면
            total += e

print(total) # 결과 출력