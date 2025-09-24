# 구슬 탈출 2
# ---> "최단 시간"을 구하는 문제라면, BFS부터 떠올려라!
from collections import deque

n, m = map(int, input().split()) # 행, 열
board = []
visited = set()

for _ in range(n): # n개의 행에 대해 입력 받기
  row = list(input().strip()) # 문자열 입력 받을 땐 유의하자
  board.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

def getPos(): # 각 공의 위치 반환
  rx, ry, bx, by = 0, 0, 0, 0
  for x in range(n):
    for y in range(m):
      if board[x][y] == 'R': # 빨간색 발견
        rx, ry = x, y
      if board[x][y] == 'B': # 파란색 발견
        bx, by = x, y
  
  return rx, ry, bx, by

def move(x, y, dx, dy): # 구슬을 움직이기 위한 함수 move
  cnt = 0
  # 이동하는 위치가 벽이 아니고, 구멍에 들어가지 않을 동안 반복
  while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
    x += dx
    y += dy
    cnt += 1 # 갯수 증가
  return x, y, cnt

def BFS():
  rx, ry, bx, by = getPos() # 빨, 파 구슬의 위치 좌표 각각 반환

  q = deque()
  q.append((rx, ry, bx, by, 1))
  visited.add((rx, ry, bx, by)) # 방문한 것에 대해 튜플로 넣기

  while q: # q가 빌 때까지
    rx, ry, bx, by, result = q.popleft()

    if result > 10: # 10번 넘어갔으면 그만둔다
      break

    for i in range(4): # 사방 탐색
      nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
      nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
    
      # 파란 구슬이 구멍에 들어간 경우
      if board[nbx][nby] == 'O':
        continue
    
      # 빨간 구슬이 들어갈 경우 성공
      if board[nrx][nry] == 'O':
        print(result)
        return
      
      # 둘이 겹쳐있을 경우 더 많이 이동한 녀석을 1칸 뒤로 보낸다
      if nrx == nbx and nry == nby:
        if rcnt > bcnt:
          nrx -= dx[i]
          nry -= dy[i]
        else:
          nbx -= dx[i]
          nby -= dy[i]
      
      # 탐색하지 않은 방향 탐색
      if (nrx, nry, nbx, nby) not in visited:
        visited.add((nrx, nry, nbx, nby))
        q.append((nrx, nry, nbx, nby, result+1))
  
  # 여기 나온거면, 못 찾은거임
  print(-1)

BFS() # BFS 함수 수행

# ============ 오답노트 ==============
# "최단 거리"를 찾는 문제라면, "BFS"를 우선적으로 고려해야 한다! (-> DFS는 모든 경로를 탐색해야 최소를 찾을 수 ㅣㅇㅆ음)
# 상태는 튜플로 묶어 방문 관리
# 파고 들어가는 느낌이 난다고 해서.. 그게 무조건 재귀로 풀어야 한다! 라는 착각에 빠져 있었음.