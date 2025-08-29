# 실전 문제 1 - 음료수 얼려 먹기
# 1 <= N, M <= 1,000
import sys
sys.setrecursionlimit(1000000) 

N, M = map(int, input().split())
board = [] # 배열 정보 저장
cnt = 0
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

for _ in range(N): # 배열 입력받기
  row = list(input())
  board.append(row)

# dfs 함수 정의
def dfs(y, x):  
  board[y][x] = '1' # 방문 표시
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if ny < 0 or ny > N - 1 or nx < 0 or nx > M - 1: # 경계 검사
      continue
    if board[ny][nx] == '1': # 칸막이라면(혹은 이미 방문했다면)
      continue
    if board[ny][nx] == '0': # 구멍이 있다면
      dfs(ny, nx) # 재귀 호출

# board 탐색
for i in range(N):
  for j in range(M):
    if board[i][j] == '0': # 구멍을 발견하면
      dfs(i, j) # 탐색 시작
      cnt += 1 # 여기 오면, 탐색 끝난거임, 셋트 하나 +1

print(cnt) # 결과 출력