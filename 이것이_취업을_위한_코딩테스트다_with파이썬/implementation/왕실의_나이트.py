# 실전 문제 1 - 왕실의 나이트 (115페이지)
# 나이트는 2가지 이동 조건이 있음, 그런데 그걸로 인해서 발생하는 최대 경우의 수는 8가지
# --> 즉, 8가지 경우 중에서 범위 벗어나는 애만 제끼면 됨

input_val = input()
row = int(input_val[1])
col = ord(input_val[0]) - ord('a') + 1  # 이렇게 하면 정확한 idx가 나올 것임

# 수평, 수직으로 이동하는 것에 대해서 dy, dx 정의
dy = [-2, -2, 2, 2, -1, -1, 1, 1]
dx = [-1, 1, -1, 1, -2, 2, -2, 2]

cnt = 0 # 가능한 경우의 수 세기 위한 변수

for i in range(8): # 길이는 8로 고정 (최대 8가지거든...)
  ny = row + dy[i]
  nx = col + dx[i]

  if nx < 1 or nx > 8 or ny < 1 or ny > 8: # 유효하지 않는 거라면 pass
    continue
  cnt += 1 # 유효한 경우면 갯수 세야지..

print(cnt) # 정답 출력
