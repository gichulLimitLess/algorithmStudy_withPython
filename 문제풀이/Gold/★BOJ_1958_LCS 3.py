# LCS 3
'''
    [사고과정]
    문자열 3개에 대한 LCS 길이를 구하라...
    음, 이거.. 3차원 dp로 풀어야 하나..? 3차원 dp 해도 되나..?
        ---> (여기서 의심을 가지고 힌트를 봤는데.. 그렇게 풀으래 / 그렇구나..)
'''
A = input()
B = input()
C = input()

# dp[i][j][k] -> A의 i번째, B의 j번째, C의 k번째까지의 원소를 고려했을 때 LCS 길이
dp = [[[0 for _ in range(len(C)+1)] for _ in range(len(B)+1)] for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        for k in range(1, len(C)+1):
            if A[i-1] == B[j-1] == C[k-1]: # 해당하는 곳들이 모두 같다면
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[len(A)][len(B)][len(C)])