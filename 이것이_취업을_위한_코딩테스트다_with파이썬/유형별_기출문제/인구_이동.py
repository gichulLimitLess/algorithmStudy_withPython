# 인구 이동
from collections import deque

# 입력 받기
n, l, r = map(int, input().split()) # 칸 수 n
board = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for _ in range(n):
  row = list(map(int, input().split()))
  board.append(row)

# board에 연합을 만들 수 있는 상황인가 확인해야 한다
def can_make_union():
  union_cnt = 0
  visited = set() # 방문 여부를 기록해야 한다
  for i in range(n):
    for j in range(n):
      for k in range(4): # 사방 탐색
        ny = i + dy[k]
        nx = j + dx[k]
        if ny < 0 or ny > n-1 or nx < 0 or nx > n-1: # 경계 검사
          continue
        # 연합 만들 수 있는 경우
        if abs(board[i][j] - board[ny][nx]) >= l and abs(board[i][j] - board[ny][nx]) <= r: 
          if (i, j) not in visited: # 이게, 이미 오늘 방문한 곳이 아니어야 한다
            BFS(i, j, visited) # 현재 칸을 시작 지점 삼아서 연합 짓기 시작
            union_cnt += 1 # 연합의 갯수 추가

  return union_cnt # 연합의 갯수 return

# 연합은 이 친구를 통해서 만든다
def BFS(start_y, start_x, visited):
  q = deque()
  q.append((start_y, start_x)) # Queue에 해당 좌표 집어 넣는다
  union = set() # union에 있는 애들은 다 여기에 넣을 것이다
  union.add((start_y, start_x)) # 연합에도 넣기
  visited.add((start_y, start_x)) # 방문한 곳으로 표시

  union_population = board[start_y][start_x] # 연합의 총 인구 수

  while q: # q가 빌 때까지
    y, x = q.popleft()
    for i in range(4): # 사방 탐색
      ny = y + dy[i]
      nx = x + dx[i]
      if ny < 0 or ny > n-1 or nx < 0 or nx > n-1: # 경계 검사
        continue
      # 연합 확장할 수 있는 경우에만
      if abs(board[y][x] - board[ny][nx]) >= l and abs(board[y][x] - board[ny][nx]) <= r: 
        if (ny, nx) not in visited: # union에 없는 경우에만
          union_population += board[ny][nx] # 연합의 인구 수 추가
          q.append((ny, nx))
          visited.add((ny, nx)) # 연합을 이루는 좌표에도 추가
          union.add((ny, nx)) # 해당 연합에 추가
  
  # 연합 안에 들어가 있는 칸들의 인구 수를 갱신해야 함
  for element in union:
    board[element[0]][element[1]] = union_population // len(union)
  
move_cnt = 0 # '인구 이동' 한 횟수 저장
while True:
  union_cnt = can_make_union() # 연합을 만들 수 있는 상황인지 판단
  if union_cnt == 0: # 더 이상 연합을 만들 수 없는 상황이라면
    break
  else:
    move_cnt += 1

print(move_cnt)