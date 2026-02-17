# 연속합
'''
    n은 최대 10만
    dp[i] = i번째까지 숫자를 고려했을 때, 구할 수 있는 합 중 가장 큰 합
'''
n = int(input())
n_arr = list(map(int, input().split()))
dp = [n_arr[i] for i in range(n)]

for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1] + n_arr[i])

print(max(dp))
