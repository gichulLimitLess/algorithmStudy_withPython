# 점화식
'''
    간단한 다이내막 프로그래밍 문제
    레츠 고도리 해보자
'''
n = int(input())
dp = [0 for _ in range(n+1)]

# 첫쩨항: 1
# dp[i] -> t(i)의 값
dp[0] = 1
for i in range(1, n+1):
    for j in range(0, i):
        dp[i] += (dp[0+j] * dp[i-1-j])

# 정답 출력
print(dp[n])