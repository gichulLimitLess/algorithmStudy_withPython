# 가장 큰 증가하는 부분 수열
# --> 수열 A의 크기 N (1 <= N <= 1000)
# dp[i]: i번째 원소를 마지막으로 하는 증가 부분 수열 중 가장 큰 합의 값

n = int(input())
A = list(map(int, input().split()))
dp = []

for i in range(len(A)): # dp의 초기 값은 각자 자기 자신으로 일단 초기화
    dp.append(A[i])

for i in range(len(A)): # 하나씩 돌면서 dp 배열 값 갱신
    for j in range(i): # i번째 수 바로 이전까지 돌면서, 증가하는 부분 수열 확인
        if A[i] > A[j]: # 증가하는 형태이면
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp)) # 합이 가장 큰 증가하는 부분 수열 합 출력
