# 치즈
'''
    [사고과정]
    - 치즈의 4개의 변 중 적어도 2개 이상의 변이 '외부 공기'와 접촉해 있을 경우.. 1시간 내로 녹아 없어지는 애들임
    - 모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정
    - 치즈 내부 공간은 비어있어도.. 공기와 접촉하지 않은 것으로 판단 --> '내부 공간 판별' 필요
    ---> Q. 입력으로 주어진 치즈가 모두 녹아 없어지는 데 걸리는 정확한 시간?
'''
from collections import deque

cheeze_cnt = 0 # 치즈 개수
time = 0 # 주어진 치즈가 모두 녹아 없어지는 데 걸리는 정확한 시간

n, m = map(int, input().split()) # 세로: n / 가로: m
board = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for e in row:
        if e == 1: # 치즈가 있다면..
            cheeze_cnt += 1

# '외부 공간'을 찾는 함수 --> O(10000)
def find_outside():
    q = deque()
    outside = set()
    q.append((0, 0))
    while q: # 큐가 빌 때까지
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
                if (ny, nx) not in outside: # 방문하지 않은 경우에만
                    outside.add((ny, nx))
                    q.append((ny, nx))
    return outside # '외부 공간' return

# outside set을 활용해서, '내부 공간'을 제외한 '외부 공간'만을 바탕으로 탐색 진행
def find_meltingCheeze(outside):
    melting_cheeze = set() # 녹아 없어질 애들 여기에 모아둘 것임
    # board를 단순히 탐색해서.. '1'일 경우에, 사방 탐색
    # --> 사방 탐색해서 outside와 겹치는 곳이 2곳 이상이면.. 지워야 할 곳들임 --> O(10000)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1: # '치즈' 발견
                cnt = 0
                for k in range(4): # 치즈는, 가장 자리에는 놓이지 않는다고 가정했으므로, 경계 검사는 필요 X
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if (ny, nx) in outside: # '외부 공간'과 접촉한다면
                        cnt += 1
                if cnt >= 2: # 2개 이상의 변과 접촉 한다면
                    melting_cheeze.add((i, j))
    return melting_cheeze

# 치즈가 다 없어질 때까지
while cheeze_cnt > 0: # ---> 이거.. 해봐야 O(10000)도 안 될 것임
    outside = find_outside() # '외부 공간' 찾기 --> O(10000)
    melting_cheeze = find_meltingCheeze(outside) # 녹아서 없어져야 할 치즈들의 좌표 찾기 ---> O(10000)
    for c_y, c_x in melting_cheeze: # 녹아서 없어져야 할 치즈들의 좌표들을 이용해, board에서 '빈칸'으로 만들기
        board[c_y][c_x] = 0
    cheeze_cnt -= len(melting_cheeze) # 치즈 개수 감소
    time += 1 # '1시간' 추가

print(time) # 주어진 치즈가 모두 녹아 없어지는 데 걸리는 정확한 시간 출력