# 실전 문제 3 - 1이 될 때까지
# N과 K가 모두 2 이상, 10만 이하
# 항상 2번 method를 선택하는 것이, 1번 method를 선택하는 것보다 효율적이거나, 동등하다
# --> N % K == 0이기만 하면, 2번을 선택하면 된다 / 아니면 1번

# N, K = map(int, input().split())

# cnt = 0
# while N > 1: # N이 1보다 큰 동안에 계속 반복
#   if N % K == 0: # 나누어 떨어지면
#     N //= K # 무조건 2번 method 선택
#     cnt += 1
#   else: # 나누어 떨어지지 않는다면
#     N -= 1 # 1번 method 선택
#     cnt += 1

# print(cnt) # 답 출력

# N, K가 각각 100억까지 커지게 되면, 위처럼 했을 때 시간 초과 on
# 좀 더 효율적으로 풀어야 함
N, K = map(int, input().split())
cnt = 0

while True: # 무한 루프 (안에 탈출 로직 있음)
  target = (N//K) * K
  cnt += (N-target) # target까지 빼야 한다
  N = target

  # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
  if N < K:
    break

  N //= K # 나눈다
  cnt += 1

cnt += (N-1) # 1까지 걸리는 걸 계산하니까, N-1만큼 cnt에 더해주기
print(cnt) # 결과 출력
