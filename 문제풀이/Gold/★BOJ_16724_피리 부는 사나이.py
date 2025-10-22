# # 피리 부는 사나이
# '''
#     n * m 크기의 지도에서 'SAFE ZONE'의 최소 개수 구하기 / n*m은 최대 100만개의 칸이 있을 수 있다, 무식하게 탐색하면 안됨
#     O(100만) 수준으로 끝내려면, 방문 처리와 SAFE ZONE 냅두는 방법에 대해서 연구할 필요 있음
#     --> 소규모의 예시들로 테스트를 해보니,
#         지도에서 방문한 곳의 좌표를 visited라는 set으로, SAFE ZONE으로 등록되어야 할 좌표를 safeArea_loc이라는 set으로 관리
#         board를 전체 탐색하며, visited에 없는 좌표(방문하지 않은 좌표인 경우)라면, board에 적혀 있는 방향 커맨드에 따라 "갈 수 있을 때까지" 간다
#         갈 수 있을 때까지 간 경우(커맨드에 따라 간 곳이 이미 방문 표시가 되어 있는 경우)라면, 그곳을 SAFE ZONE이 가능한 곳으로 표기 후 탈출
# '''
# # 입력 받기
# n, m = map(int, input().split())
# board = []
# for _ in range(n):
#     row = list(input())
#     board.append(row)
# print(board)
#
# safeZone_loc = set() # "SAFE ZONE" 위치 표기한 set
# visited = set() # 방문한 좌표 위치 표기한 set
# # 방향 커맨드 --> "위 -> 아래 -> 왼쪽 -> 오른쪽" 순서
# dy = [-1, 1, 0, 0]
# dx = [0 ,0, -1, 1]
#
# # 막혔는지 확인하는 is_blocked()
# def is_blocked(ny, nx):
#     if (ny, nx) in visited or (ny, nx) in safeZone_loc: # 지금 가려는 방향이 이미 지나온 곳이거나, safe zone이라면?
#         return True
#     return False
#
# # 갈 수 있을때 까지 가보는 search_area 함수
# def search_area(y, x):
#     ny = y
#     nx = x
#     # "지도 바깥으로 나가는 방향의 입력은 주어지지 않으므로, "경계 검사"는 할 필요 X
#     while True:
#         # 방문하지 않은 곳을 방문한다면, 일단 방문 표시부터 하고 탐색 진행한다
#         visited.add((y, x))
#         no_more = False
#         if board[y][x] == 'U': # 위로 가야 하는 경우
#             ny = y + dy[0]
#             nx = x + dx[0]
#             no_more = is_blocked(ny, nx)
#         elif board[y][x] == 'D': # 아래로 가야 하는 경우
#             ny = y + dy[1]
#             nx = x + dx[1]
#             no_more = is_blocked(ny, nx)
#         elif board[y][x] == 'L': # 왼쪽으로 가야 하는 경우
#             ny = y + dy[2]
#             nx = x + dx[2]
#             no_more = is_blocked(ny, nx)
#         elif board[y][x] == 'R': # 오른쪽으로 가야 하는 경우
#             ny = y + dy[3]
#             nx = x + dx[3]
#             no_more = is_blocked(ny, nx)
#
#         if no_more: # 더 이상 진행이 불가하다면
#             safeZone_loc.add((y, x)) # 그곳이 "SAFE ZONE"이 되어야 한다
#             return # 무한루프 탈출 및 함수 종료
#         else:
#             y = ny
#             x = nx
#
# # board 전체를 탐색하며 진행
# for i in range(n):
#     for j in range(m):
#         if (i, j) not in visited: # 방문하지 않은 칸에 대해서만 탐색 진행
#             search_area(i, j)
#
# print(safeZone_loc) # 디버깅용
# print(len(safeZone_loc)) # 여기에 저장되어 있는 safeZone_loc의 길이가 결국 'SAFE ZONE'의 최소 개수

# ======================== 정답 코드 =============================
