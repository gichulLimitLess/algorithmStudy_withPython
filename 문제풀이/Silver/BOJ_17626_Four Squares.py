# Four Squares
'''
    dp 문제 한 번 풀어보자
'''
from math import sqrt

INF = float('inf')
n = int(input())
dp = [INF for _ in range(n+1)]
# 초기값 설정
dp[0] = 0
dp[1] = 1

# 하나씩 dp 테이블 채워 나가기 --> O(5만 * 250)
for i in range(2, n+1):
    for j in range(1, int(sqrt(i))+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)

print(dp[n])