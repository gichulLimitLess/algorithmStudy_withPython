# 아기 상어
from collections import deque

INF = int(1e9)

def BFS(board, start, now_shark_size):
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    q = deque()
    q.append((start[0], start[1], 0)) # queue에 맨 처음 꺼 넣기
    eat_candidate = [] # 먹을 수 있는 물고기들의 후보를 eat_candidate에 저장
    min_dist = INF
    visited = set() # 방문 처리는 visited에 진행할 것임

    while q: # queue가 빌 때까지
        y, x, dist = q.popleft()
        if board[y][x] != 0 and now_shark_size > board[y][x]: # 빈 곳이 아니고, 먹을 수 있다면..
            if min_dist > dist: # 더 짧은 경로에서의 물고기 발견
                eat_candidate = [(y, x, dist)] # 아예 얘가 더 가까운 애임
                min_dist = dist
            elif min_dist == dist: # 같은 거리에 있는 물고기라면
                eat_candidate.append((y, x, dist))

        for i in range(4): # 사방 탐색
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny <= len(board)-1 and 0 <= nx <= len(board[0])-1: # 유효한 범위에서만 탐색
                if (ny, nx) in visited: # 방문한 곳이라면
                    continue
                if board[ny][nx] <= now_shark_size: # 현재 상어 크기보다 작거나 같을 때만 "이동" 가능
                    q.append((ny, nx, dist+1))
                    visited.add((ny, nx)) # 방문 표시

    return eat_candidate # 먹을 수 있는 후보군들 return


now_eat_cnt = 0 # 먹은 물고기 갯수
now_shark_size = 2 # 현재 상어 크기 (-> 최초의 크기는 2)
total_time = 0 # 총 걸린 시간 (-> 최종적으로 엄마 상어에게 도움 요청하러 갈 때, 이를 반환할 것임)
now_shark_location = [0, 0] # 초기 값은.. board 입력 받을 때 여기에 초기화 될 것임

n = int(input()) # n 입력 받기
board = []
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(n): # 아기 상어 있는지 체크
        if row[j] == 9: # 아기 상어 위치 발견
            now_shark_location[0] = i
            now_shark_location[1] = j

while True: # 엄마 상어에게 도움을 요청하러 갈 때까지 계속 진행
    eat_candidate = BFS(board, now_shark_location, now_shark_size) # 탐색 수행.. 누굴 잡아먹을 수 있는지..
    if len(eat_candidate) == 0: # 먹을 수 있는 물고기가 공간에 없다고 판단되는 경우
        break
    elif len(eat_candidate) == 1: # 먹을 수 있는 물고기가 1마리만 딱 있다면
        y = eat_candidate[0][0]
        x = eat_candidate[0][1]
        total_time += eat_candidate[0][2] # 시간 dist 값 ++
        board[y][x] = 9 # 그곳으로 '아기 상어'가 이동한다
        board[now_shark_location[0]][now_shark_location[1]] = 0 # 이전에 아기 상어가 있던 곳은 '빈칸'으로 표기
        now_shark_location[0] = y
        now_shark_location[1] = x
        now_eat_cnt += 1 # 먹은 물고기 수 +1
        if now_shark_size == now_eat_cnt: # 자신의 크기와 같은 수의 상어를 먹었다면
            now_shark_size += 1 # 크기 1 증가
            now_eat_cnt = 0
    else: # 먹을 수 있는 애가 여러명이라면
        eat_candidate.sort(key= lambda x: (x[0], x[1])) # 가장 위, 그 위의 좌표가 같다면 가장 왼쪽부터.. 하도록 정렬
        y = eat_candidate[0][0]
        x = eat_candidate[0][1]
        total_time += eat_candidate[0][2]  # 시간 dist 값 ++
        board[y][x] = 9  # 그곳으로 '아기 상어'가 이동한다
        board[now_shark_location[0]][now_shark_location[1]] = 0  # 이전에 아기 상어가 있던 곳은 '빈칸'으로 표기
        now_shark_location[0] = y
        now_shark_location[1] = x
        now_eat_cnt += 1 # 먹은 물고기 수 +1
        if now_shark_size == now_eat_cnt:  # 자신의 크기와 같은 수의 상어를 먹었다면
            now_shark_size += 1  # 크기 1 증가
            now_eat_cnt = 0

print(total_time) # 최종 결과 출력 (== 엄마 상어에게 도움 요청하지 않고 물고기를 잡아먹을 수 있는 시간)