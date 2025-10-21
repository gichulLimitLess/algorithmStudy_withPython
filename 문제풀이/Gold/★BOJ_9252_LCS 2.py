# LCS
# --> LCS 유형 복습 겸, DP 익숙해질 겸 진행
first = input()
second = input()

# dp[i][j] -> first의 i번째까지만의 원소를 고려하고, second의 j번째까지만의 원소를 고려했을 때,
#             그때 당시까지의 LCS 길이

dp = [[0 for _ in range(len(second))] for _ in range(len(first))]
dp_lcs = [['' for _ in range(len(second))] for _ in range(len(first))]

# dp 배열 초깃값 설정 (--> 첫번째 행과, 첫 번째 열을 초기화 해야 함)
# dp의 첫번째 행(row) 초기화
for j in range(1, len(second)):
    dp[0][j] = 1 if first[0] == second[j] else dp[0][j-1]
    dp_lcs[0][j] = first[0] if first[0] == second[j] else dp_lcs[0][j-1]

# dp의 첫번째 열(col) 초기화
for i in range(1, len(first)):
    dp[i][0] = 1 if first[i] == second[0] else 0
    dp_lcs[i][0] = first[i] if first[i] == second[0] else ''

# dp 배열 하나씩 채워 나가기 --> O(1000 * 1000) == O(100만)
for i in range(1, len(first)):
    for j in range(1, len(second)):
        if first[i] == second[j]: # 같다면
            # 해당하는 값들을 업데이트하여 "누적"한다 (lcs 포함)
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j] = dp[i][j-1]
                dp_lcs[i][j] = dp_lcs[i][j-1]
            else:
                dp[i][j] = dp[i-1][j] + 1
                dp_lcs[i][j] = dp_lcs[i][j-1] + second[j]
        else: # 다르다면
            # 해당하는 값들을 업데이트하여 "누적"한다 (lcs 포함)
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j] = dp[i][j-1]
                dp_lcs[i][j] = dp_lcs[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
                dp_lcs[i][j] = dp_lcs[i-1][j]

print(dp_lcs)
print(dp[len(first)-1][len(second)-1]) # 두 문자열의 lcs 길이
print(dp_lcs[len(first)-1][len(second)-1]) # lcs 출력