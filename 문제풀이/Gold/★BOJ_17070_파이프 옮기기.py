# # 파이프 옮기기
# '''
#     [사고과정]
#     집의 크기 N (3 <= N <= 16) --> 충분히 모든 경우의 수에 대해 DFS로 브루트포스 해도 될 듯
#     각 보드 상황에 대해서, 독립성을 보장해야 하므로, deepcopy를 해야 할 듯
#     --> 그리고.. board에서 무조건 오른쪽, 아래, 오른쪽 아래로만 이동 가능하므로, 방문 처리 따로 필요 없음
#         (무조건, n, n으로 이동하는 방향으로 설계되어 있음)
#     --> dir 방향 설계:
#         0 => 가로 / 1 => 세로 / 2 => 대각선
#     --> 시간 복잡도는.. 최악의 경우에도 O(3^15) --> O(2000만) 정도로 충분히 해결 가능할 듯
# '''
#
# n = int(input()) # 집의 크기 n
# board = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     board.append(row)
#
# # 맨 오른쪽 or 아래쪽 좌표 기준으로, 이동하려는 방향에 따라 확인해야 할 빈칸 좌표를 저장해 놓은 dict
# # key: (현재 방향, target 방향), value: (맨 오른쪽 또는 아래 좌표 기준으로 확인해야 할 좌표 가중치)
# dir_dict = {
#     (0,0): [(0,1)],
#     (0,2): [(1,0), (1,1), (0,1)],
#     (1,1): [(1,0)],
#     (1,2): [(1,0),(1,1),(0,1)],
#     (2,0): [(0,1)],
#     (2,1): [(1,0)],
#     (2,2): [(1,0),(1,1),(0,1)]
# }
#
# # 이동하려는 방향으로 가능한지 확인하는 것
# def can_move(dir, nxt_dir, np):
#     combi_list = dir_dict[(dir, nxt_dir)]
#     for combi in combi_list: # 가능한 방향 모두 뒤져보면서 확인
#         ny = np[1][0] + combi[0]
#         nx = np[1][1] + combi[1]
#         if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 1: # 경계 검사
#             continue
#         else: # 경계에 걸려도, false
#             return False
#
#     return True # 여기까지 살아 있었다면 True
#
# cnt = 0
# # dir 값에 대해.. 0: 가로 / 1: 세로 / 2: 대각선
# def search(dir, np):
#     if np[1][0] == n-1 and np[1][1] == n-1: # 한쪽 끝이 (n,n)에 도달
#         global cnt
#         cnt += 1
#         return
#
#     if dir == 0: # 현재 방향이 가로일 경우
#         # 이동할 수 있는 방향 2가지 --> 오른쪽, or 오른쪽 아래
#         if can_move(dir, 0, np): # 1. 오른쪽으로 이동 가능한지 검사
#             nnp = np[1:]
#             nnp.append((nnp[0][0], nnp[0][1]+1)) # 새로운 애를 집어 넣는다
#             search(0, nnp) # '가로 방향' 유지한 채로 계속 탐색
#
#         if can_move(dir, 2, np): # 2. 오른쪽 아래로 이동 가능한지 검사
#             nnp = np[1:]
#             nnp.append((nnp[0][0]+1, nnp[0][1]+1))  # 새로운 애를 집어 넣는다
#             search(2, nnp)  # '대각선 방향'으로 변경 후 계속 탐색
#
#     if dir == 1: # 현재 방향이 세로일 경우
#         # 이동할 수 있는 방향 2가지 --> 아래 or 오른쪽 아래
#         if can_move(dir, 1, np): # 1. 아래쪽으로 이동 가능한지 검사
#             nnp = np[1:]
#             nnp.append((nnp[0][0]+1, nnp[0][1])) # 새로운 애 집어넣기
#             search(1, nnp)
#
#         if can_move(dir, 2, np): # 2. 오른쪽 아래로 이동 가능한지 검사
#             nnp = np[1:]
#             nnp.append((nnp[0][0]+1, nnp[0][1]+1))
#             search(2, nnp)
#
#     if dir == 2: # 현재 방향이 대각선일 경우
#         # 이동할 수 있는 방향 3가지 --> 가로, 세로, 대각선
#         if can_move(dir, 0, np): # 1. 가로로 이동 가능한지 검사
#             nnp = np[1:]
#             nnp.append((nnp[0][0], nnp[0][1]+1))
#             search(0, nnp)
#
#         if can_move(dir, 1, np): # 2. 세로로 이동 가능한지 검사
#             nnp = np[1:]
#             nnp.append((nnp[0][0]+1, nnp[0][1]))
#             search(1, nnp)
#
#         if can_move(dir, 2, np): # 3. 대각선으로 이동 가능한지 검사
#             nnp = np[1:]
#             nnp.append((nnp[0][0]+1, nnp[0][1]+1))
#             search(2, nnp)
#
# search(0, [(0,0), (0,1)]) # 탐색 시작
# print(cnt) # 결과 출력

# ============= 위는 오답 풀이 --> 전체 DFS 브랜치는 3^(n*n)에 가까운 폭발적으로 늘어난다 ========
# 따라서 위는.. dp로 풀어야 한다
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# dp[y][x][d] : (y,x)에 파이프 끝이 있고 방향 d(0=가로,1=세로,2=대각선)일 때 경우의 수
dp = [[[0] * 3 for _ in range(n)] for __ in range(n)]

dp[0][1][0] = 1  # 초기 파이프는 (0,0)-(0,1) 가로

for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            continue

        # 가로 → (y, x+1)
        if x + 1 < n and board[y][x + 1] == 0:
            dp[y][x + 1][0] += dp[y][x][0] + dp[y][x][2]

        # 세로 → (y+1, x)
        if y + 1 < n and board[y + 1][x] == 0:
            dp[y + 1][x][1] += dp[y][x][1] + dp[y][x][2]

        # 대각선 → (y+1, x+1)
        if (x + 1 < n and y + 1 < n
                and board[y][x + 1] == 0
                and board[y + 1][x] == 0
                and board[y + 1][x + 1] == 0):
            dp[y + 1][x + 1][2] += dp[y][x][0] + dp[y][x][1] + dp[y][x][2]

print(sum(dp[n - 1][n - 1]))
