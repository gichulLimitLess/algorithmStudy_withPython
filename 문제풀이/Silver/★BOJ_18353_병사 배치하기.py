# 병사 배치하기
n = int(input())
soldiers = list(map(int, input().split()))

# LIS 문제로 변환하기 위한 테크닉
soldiers.reverse()

# dp[i] -> i번째를 가장 마지막 원소로 갖는 부분수열 중에서, 가장 긴 증가 부분 수열의 길이
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if soldiers[j] < soldiers[i]: # 오름차순 만족하면
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp)) # 열외해야 할 최소 병사 수 출력

'''
    [오답노트]
    -> LIS, 배낭 문제 등.. DP의 핵심 유형들을 꼭 알아두자.
    -> 여기서도, LIS 문제 쓰였다!
'''