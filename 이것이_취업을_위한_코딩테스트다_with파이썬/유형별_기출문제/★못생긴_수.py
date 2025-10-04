# 못생긴 수
# --> 오직, 2,3,5(1 포함)만을 소인수로 가지는 수 == 못생긴 수

n = int(input())
dp = [0 for _ in range(n+1)] # dp[i] -> i번째 못생긴 수
dp[1] = 1
two_idx = 1
three_idx = 1
five_idx = 1

for i in range(2, n+1):
    next2 = dp[two_idx] * 2
    next3 = dp[three_idx] * 3
    next5 = dp[five_idx] * 5

    res = min(next2, next3, next5) # 가장 최솟값 가져온다
    dp[i] = res

    if res == dp[two_idx] * 2: # 2를 곱한거랑 값이 같다면
        two_idx += 1
    if res == dp[three_idx] * 3: # 3을 곱한거랑 값이 같다면
        three_idx += 1
    if res == dp[five_idx] * 5: # 5를 곱한거랑 값이 같다면
        five_idx += 1

print(dp[-1])