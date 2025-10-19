# 청소년 상어
import copy

# Step1. 물고기 위치 정보 입력 받기
board = []
for _ in range(4):
    info_list = list(map(int, input().split()))
    row = []
    for i in range(0, len(info_list), 2): # step을 2개씩 밟아간다
        row.append([info_list[i], info_list[i+1]-1]) # (물고기 번호, 방향 정보) 주입
    board.append(row) # board의 한 줄에 이렇게 넣는다

# Step2. 필요한 변수들 추가
# 1(윗방향)을 기점으로 반시계 45도 회전하는 방향으로 진행하도록 dy, dx 배열 선언
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

max_sum = 0 # 상어가 먹을 수 있는 물고기 번호의 합 저장

# 현재 board(now_board)에서 물고기의 위치를 찾는 함수
def find_fish_location(fish_num, now_board):
    for i in range(4):
        for j in range(4):
            if now_board[i][j][0] == fish_num: # 찾았다면, (i,j) 리턴
                return i, j
    return -1, -1 # 못 찾았다면, -1 리턴

# 상어 움직이는 함수
# 상어가 먹을 수 있는 물고기 번호의 합의 최대는.. 언제 어디서 최대가 될지 모른다
# DFS를 통해서 모든 경우를 "완전 탐색" 해야 한다
def dfs(sy, sx, score, now_board):
    global max_sum
    score += now_board[sy][sx][0] # 현재 먹은 물고기 번호만큼 ++
    max_sum = max(score, max_sum) # 최댓값 계속 갱신해 준다
    now_board[sy][sx][0] = 0 # 상어가 먹었으니, 여기는 이제 물고기가 없는(빈칸) 표시한다

    # 물고기 움직임
    for f_num in range(1, 17): # 물고기는 무조건 1번부터 16번까지 밖에 없음
        # 어차피, 그 물고기의 y, x 좌표를 찾아야 한다 -> board 크기 4*4 밖에 안되므로 탐색 진행
        f_y, f_x = find_fish_location(f_num, now_board)
        if f_y != -1 and f_x != -1: # 존재하는 경우에만 진행
            # 지금 물고기 방향 불러오기, 그릐고 8방 탐색
            f_d = now_board[f_y][f_x][1]
            for i in range(8):
                ny = f_y + dy[(f_d+i)%8]
                nx = f_x + dx[(f_d+i)%8]
                if 0 <= ny <= 3 and 0 <= nx <= 3: # 경계 검사 통과한 경우에만
                    # 빈칸은 0, 물고기 번호는 무조건 1부터 16.. 따라서 범위로 표현해도 ok
                    # 상어가 있는 곳이어도 안된다
                    if 0 <= now_board[ny][nx][0] <= 16 and not (ny == sy and nx == sx):
                        # 바뀐 방향 업데이트, 자리 바꿈, 그리고 종료
                        now_board[f_y][f_x][1] = (f_d + i) % 8
                        now_board[ny][nx], now_board[f_y][f_x] = now_board[f_y][f_x], now_board[ny][nx]
                        break

    # 상어의 움직임
    s_d = now_board[sy][sx][1] # 상어 방향
    # 상어는 최대 4번까지 해당 방향의 자리 탐색 가능
    for i in range(1, 5):
        ny = sy + dy[s_d] * i
        nx = sx + dx[s_d] * i
        # 이동 가능한 자리인지 체크한 뒤에 dfs
        if (0 <= ny < 4 and 0 <= nx < 4) and now_board[ny][nx][0] > 0:
            dfs(ny, nx, score, copy.deepcopy(now_board)) # board는 매 순간 달라지므로, deepcopy 떠야 함

dfs(0, 0, 0, copy.deepcopy(board)) # dfs 수행
print(max_sum) # 최댓값 출력