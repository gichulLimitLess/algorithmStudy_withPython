# 감시 피하기
n = int(input())
board = []
teacher_location = [] # 선생님들 위치 표시

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# board 입력받기
for i in range(n):
  row = list(input().split(' '))
  for j in range(n): # row에 대해서, 선생님 위치 파악
    if row[j] == 'T': # 선생님이면  
      teacher_location.append((i, j)) # (행, 열) 순서
  board.append(row)

# 벽에 닿을 때까지 각 방향에 대해서 학생이 있는지 검사
def noOne(direction, y, x, n):
  if y < 0 or y > n-1 or x < 0 or x > n-1 or board[y][x] == 'O': # 벽 혹은 장애물이 있다면
    return True
  if board[y][x] == 'S': # 학생을 발견했으면
    return False  
  return noOne(direction, y + dy[direction], x + dx[direction], n) # 재귀 호출

# 장애물 board에 찍어내고, 가능한지 판별
def check_possibility(cnt):
  if cnt == 3: # 장애물 3개 모두 찍어냈다면
    for location in teacher_location: # 선생님들 있는 위치로부터 하나씩 확인
      for i in range(4): # 4가지 방향에 대해서 쭉 탐색
        res = noOne(i, location[0]+dy[i], location[1]+dx[i], n) # 해당 방향으로 학생 있나 검사
        if res == False: # 학생이 있다면, 더 이상 탐색할 필요가 없다
          return "NO"
    return "YES" # 여기까지 왔으면, 다 통과한거다

  # 보드 탐색 -> 빈 곳에다가 'O'(장애물) 찍을거임
  for i in range(n):
    for j in range(n):
      if board[i][j] == 'X': # 빈 곳이면
        board[i][j] = 'O' # 장애물 표시
        res = check_possibility(cnt+1) # 재귀 호출
        if res == "YES": # Yes일 경우에만 Yes 하고, 아니면 그냥 재개한다
          return "YES"
        board[i][j] = 'X' # 장애물 표시한 곳을 다시 비워두기
  
  return "NO" # 여기까지 왔으면, 3개의 장애물로 학생들을 다 가릴 수 없던 것

print(check_possibility(0)) # 결과 출력