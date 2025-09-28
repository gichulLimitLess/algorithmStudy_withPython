# 불
# '상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다'
# '불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 상근이는 이동할 수 없다' --> 여기에서, '불'부터 이동 시켜야 하는 것을 알 수 있다
from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def BFS(board, queue, w, h): # --> 여기에서, 최악의 시간 복잡도: O(1000 * 1000 * 2)
  while queue: # queue가 빌 때까지
    kind, y, x, time = queue.popleft()
    if kind == '*': # 불이면, 단순히 퍼지기만 하면 된다
      for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny > h-1 or nx < 0 or nx > w-1: # 경계 검사
          continue
        if board[ny][nx] == '#' or board[ny][nx] == '*': # 벽이 있거나, 이미 불이 붙었다면 (-> 상근이가 남기고 간 자취는 없애버려야 하니 여기서 배제)
          continue
        queue.append(('*', ny, nx, time+1)) # 불 정보를 queue에 넣는다
        board[ny][nx] = '*' # 불 표시
    elif kind == '@': # 상근이일 경우
      for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny > h-1 or nx < 0 or nx > w-1: # 경계 검사 (-> 출구로 나온 경우)
          return time+1
        if board[ny][nx] == '#' or board[ny][nx] == '*' or board[ny][nx] == '@': # 벽이 있거나, 불이 있는 경우 (불이 옮겨진 칸과 불이 붙으려는 칸 모두 반영되었음, 이미 왔던 경로도 pass)
          continue
        queue.append(('@', ny, nx, time+1)) # 불 정보를 queue에 넣는다
        board[ny][nx] = '@' # 불 표시

  return -1 # 못 찾았다면, -1 리턴

tc = int(input())
for _ in range(tc): # 테스트 케이스만큼 반복
  w, h = map(int, input().split()) # 너비 w, 높이 h 입력
  board = []
  user_startInfo = tuple()
  queue = deque()

  for i in range(h): # 한 줄씩 입력 받기
    row = list(input())
    board.append(row)
    for j in range(w): # 입력 받은 row에서 탐색
      if board[i][j] == '@': # 상근이의 시작 위치 발견
        user_startInfo = ('@', i, j, 0)
      elif board[i][j] == '*': # 불 위치 발견 (-> 불부터 queue에 넣어서 처리해야 한다)
        queue.append(('*', i, j, 0))
  
  queue.append(user_startInfo) # '상근이'의 시작 위치는 나중에 넣는다
  result = BFS(board, queue, w, h) # BFS 수행
  if result == -1: # 못 찾았으면
    print("IMPOSSIBLE")
  else: # 찾았으면
    print(result)