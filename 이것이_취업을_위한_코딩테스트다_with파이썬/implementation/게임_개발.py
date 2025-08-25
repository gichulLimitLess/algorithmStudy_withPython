# 실전 문제 2 - 게임 개발 (118페이지)

# 복잡한 요구사항들이 있는 문제이다. 차근차근 따라가야 할 것이다

# 1. 우선 입력 처리
N, M = map(int, input().split(' '))
A, B, d = map(int, input().split(' '))
board = []

for _ in range(N): # N개의 줄에 걸쳐 행들 입력 받기
  row = list(input().split(' ')) # 행 입력
  board.append(row)

board[A][B] = '#' # 캐릭터가 최초 위치하는 곳 일단 방문 처리

# 2. 바라보는 방향에 따라 매뉴얼 처리
cnt = 1 # 방문한 칸 수 세기 위한 변수
dy = [-1, 0, 1 ,0]
dx = [0, 1, 0, -1] # d(방향) 자체를 인덱스로 활용하기 위해 북/동/남/서 순서 맞춤

while True: # 주어진 매뉴얼대로 while문 동작
  rotate_cnt = 0 # 현재 자리에서 몇 번 회전했는지 계산해야 함 (4번일 경우, 뒤로 가는 경우 추가 고려, 거기에서 뒤가 바다이면 중지)
  while rotate_cnt < 4: # 4번 돌 때까지 계속 반복
    d = d - 1 # 반시계 방향으로 90도 회전하는 효과가 있음
    if d < 0: # 지속적으로 d를 빼니까, 예외는 이 경우에만 발생
      d = 3
    ny = A + dy[d]
    nx = B + dx[d]

    if ny < 0 or ny > N-1 or nx < 0 or nx > M-1: # 경계 검사 (경계 바깥은 다 바다니까)
      rotate_cnt += 1
      continue
    elif board[ny][nx] == '1' or board[ny][nx] == '#': # 가려는 위치가 이미 방문한 곳이거나 바다인 경우
      rotate_cnt += 1
      continue
    
    # 위의 예외 사항들을 모두 통과해야, 비로소 이동 가능하다
    A = ny
    B = nx
    board[A][B] = '#'
    cnt += 1
    break # 반목문 탈출
  
  if rotate_cnt == 4: # 4번 돌았다면, 사방이 못 가는 상황
    d = d - 1 # 반시계 방향으로 90도 회전하는 효과가 있음
    if d < 0: # 지속적으로 d를 빼니까, 예외는 이 경우에만 발생
      d = 3
    ny = A - dy[d]
    nx = B - dx[d]
    
    if board[ny][nx] == '1': # 뒤로 갔는데 바다이면..
      break # 이동 종료

print(cnt)


  

