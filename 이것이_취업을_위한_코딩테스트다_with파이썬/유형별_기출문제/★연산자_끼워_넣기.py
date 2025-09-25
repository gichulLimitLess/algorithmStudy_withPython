# 연산자 끼워 넣기
# --> 음수의 나눗셈인 경우, 양수로 바꿔서 몫을 취하고, 그것을 음수로 바꾸는 추가 과정이 필요!
# --> DFS로 연산자에 대한 쌍을.. 순열로 구하는 듯한 느낌으로 접근하자.

n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))

# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최소, 최대 초기화
min_value = float('inf')
max_value = -float('inf')

# dfs 메소드
def dfs(i, now):
  global min_value, max_value, add, sub, mul, div
  # 모든 연산자를 다 사용한 경우, 최소/최대 업데이트
  if i == n:
    min_value = min(min_value, now)
    max_value = max(max_value, now)
    return
  
  # 각 연산자에 대해서 계산 수행
  if add > 0:
    add -= 1
    dfs(i+1, now+data[i])
    add +=1
  if sub > 0:
    sub -= 1
    dfs(i+1, now-data[i])
    sub += 1
  if mul > 0:
    mul -= 1
    dfs(i+1, now*data[i])
    mul += 1
  if div > 0:
    div -= 1
    if now < 0: # now가 음수일 때
      dfs(i+1, -(abs(now) // data[i]))
    else: # 나머지는 그대로 파이썬의 정수 나눗셈 사용
      dfs(i+1, (now // data[i])) # 나눌 때는 나머지를 제거
    div += 1

# dfs 메소드 호출
dfs(1, data[0])

# 최대, 최소 차례대로 출력
print(max_value)
print(min_value)