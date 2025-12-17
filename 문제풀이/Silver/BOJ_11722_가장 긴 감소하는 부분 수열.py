# 가장 긴 감소하는 부분 수열
'''
    LIS 복습하는 차원에서 레츠고
'''
n = int(input())
n_list = list(map(int, input().split()))

# dp[i] -> i번째 원소를 마지막 원소로 하는 가장 긴 감소하는 부분 수열의 길이
dp = [1 for _ in range(n)]
for i in range(1, n):
    min_val = n_list[i]
    for j in range(i):
        if n_list[j] > min_val: # "감소하는 부분 수열" 조건을 만족하는 경우
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp)) # "가장 긴 감소하는 부분 수열"의 '길이' 구하기