# 불!
'''
    [사고과정]
    - 지훈이가 미로를 탈출할 수 있는 경우 --> 미로의 가장자리에 접한 공간에 갔을 경우
    - 지훈이가 탈출할 수 없는 경우
        --> '불'에 둘러 싸이거나, '벽'에 둘러 싸여 못 나가는 경우
    - 그러면.. '불 이동' -> '지훈이 이동'을 차례차례 Queue에 집어 넣으면서,
        지훈이가 가장자리에 도달했을 경우, 바로 그 당시의 '탈출 시간' 값을 return 해서 끝내면 되는 거 아님?
        그리고, Queue가 빌 때까지 지훈이가 탈출 못 했으면, 그게 바로 impossible 아님?
    - '불'은, '벽'만 통과 못하는 것임 --> 지훈이가 남기고 간 자취는 그냥 자기로 덮어 씌우기 가능
    - '지훈이'는, '벽' 뿐만 아니라, '불' 또한 통과할 수 없음 (그럼 불에 타버리잖아..)
    - 그런데, 특수 케이스가 있을 수 있다.. '불'과 '지훈이'의 상태가 서로 오염되면 안되는 것 같다
        --> 지훈이가 이미 불에 타버리면, 종료해야 하는데, 불에 탄 상황에서도 계속 이동해 버리게 된다
            (Queue에 그 상태가 남아 있어서..)
        --> 배열 따로 관리하면 되는 거 아님? (jihun_board, fire_board)
'''
from collections import deque

r, c = map(int, input().split())
# --> 여기 board 3개 해봤자.. 최대 12MB 될까?
board = []
q = deque()
jihun_board = [[False for _ in range(c)] for _ in range(r)] # 지훈이 방문 여부 표시 (--> fire_board랑 board 보고 이동 여부 판단)
fire_board = [[False for _ in range(c)] for _ in range(r)] # 불 방문 여부 표시 (--> board 보고 이동 여부 판단)
first_jihun = []

for i in range(r):
    row = input()
    for j in range(c):
        if row[j] == 'J': # 지훈이의 초기 위치 발견
            first_jihun = [i, j]
            jihun_board[i][j] = True
        elif row[j] == 'F': # 불의 초기 위치 발견 했다면
            q.append(('F', i, j, 0))
            fire_board[i][j] = True
    board.append(row)

q.append(('J', first_jihun[0], first_jihun[1], 0)) # '불 이동' -> '지훈이 이동' 순으로 진행되어야 한다

# 지훈이와 불의 이동을 진행한다 --> 불부터 움직이고, 지훈이 이동 시킨다
# 예상 시간 복잡도: 모든 칸을 딱 한 번씩만 방문: O(100만)
def simulation():
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    while q:
        case, y, x, time = q.popleft()
        # 1. '불'이라면 fire_board에서 이동 시킨다
        if case == 'F':
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= ny < r and 0 <= nx < c:
                    # --> 이동하려는 칸이 '벽'이 아니면서, 이미 방문한 곳이 아닐 때만
                    if board[ny][nx] != '#' and not fire_board[ny][nx]:
                        fire_board[ny][nx] = True
                        q.append(('F', ny, nx, time+1))

        # 2. '지훈이'라면, jihun_board에서 이동 시킨다
        if case == 'J':
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if ny < 0 or ny >= r or nx < 0 or nx >= c: # 가장자리에 도달했다면, 바로 return
                    return time+1
                if 0 <= ny < r and 0 <= nx < c:
                    # ---> 이동하려는 칸이 '벽'이 아니면서, 불이 없으면서, 지훈이가 이미 방문한 곳이 아니어야 함
                    if board[ny][nx] != '#' and not fire_board[ny][nx] and not jihun_board[ny][nx]:
                        jihun_board[ny][nx] = True
                        q.append(('J', ny, nx, time+1))

    return -1 # 여기까지 왔으면, 지훈이는 탈출 실패한 거임

answer = simulation()
# 정답 출력
if answer == -1:
    print('IMPOSSIBLE')
else:
    print(answer)