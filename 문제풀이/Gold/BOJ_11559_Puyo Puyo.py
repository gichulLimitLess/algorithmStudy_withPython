# Puyo Puyo
'''
    입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태
    --> 연결되어 있는 같은 색 뿌요들은 한꺼번에 없어진다 (그것이 4개인지 확인)

    [설계한 알고리즘]
    1. 위에서부터 아래로 board 탐색
    2. '색깔있는 블록(R, G, B, P, Y)'을 만났을 경우
        -> 상하좌우 BFS 수행 (같은 것이 있는지 지속적으로 확인)
        -> 그것의 개수가 4개 이상으로 count 되었을 경우
            들어온 좌표들 전부 '.'으로 만들기
            '연쇄'가 일어난다고 표시 (isFound = True)
    3. (연쇄반응이 있었을 때만) 맨 밑에줄 기준으로 한 열씩 위로 올라가며 중력으로 끌어 내리기
'''
from collections import deque

board = []
for _ in range(12):
    board.append(list(input()))
combo = 0 # 현재 주어진 상황에서 몇연쇄가 되는지 저장하는 변수

# 1단계에서 같은 뿌요 4개 이상 모여서 없어지는지 확인
def BFS(y, x, color):
    q = deque()
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    visited = set()
    candidates = [] # 없어질 후보들 (길이가 4 이상이어야만 없어짐)
    q.append((y, x)) # 시작 지점 넣기
    visited.add((y, x))
    candidates.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            # 방문하지 않았고, 경계 내부에만 있어야 추가할 수 있죠
            if 0 <= ny < 12 and 0 <= nx < 6 and (ny, nx) not in visited:
                if board[ny][nx] == color: # 같은 색깔이어야 한다
                    visited.add((ny, nx))
                    candidates.append((ny, nx))
                    q.append((ny, nx))
    return candidates # 방문한 애들 모두 돌려주기

# 3단계에서 빈 공간에 대해 한 열씩 중력으로 끌어내리는 gravity 함수
def gravity(x):
    for j in range(11, -1, -1):
        k = j
        while k > 0 and board[k][x] == '.': # 색깔있는 곳 처음 도달할 때까지
            k -= 1
        board[k][x], board[j][x] = board[j][x], board[k][x] # 값 바꾸기

while True:
    # 1. 위에서부터 아래로 board 탐색
    isFound = False # '연쇄' 작용이 일어났는지 확인하는 Flag 값
    for i in range(12):
        for j in range(6):
            # 2. '색깔있는 블록(R, G, B, P, Y)'을 만났을 경우
            if board[i][j] != '.':
                candidates = BFS(i, j, board[i][j])
                if len(candidates) >= 4: # 길이가 4 이상이라면 --> '없어져야 함' & 연쇄 +1
                    for y, x in candidates:
                        board[y][x] = '.' # 빈공간으로 처리
                        isFound = True
    if isFound: # '연쇄' 반응이 한 번이라도 있었다면
        combo += 1
        # 3. 맨 밑에줄 기준으로 한 열씩 위로 올라가며 중력으로 끌어 내리기
        for i in range(6):
            gravity(i)
    else:
        break

# 결과 출력
print(combo)