# [백준 9252 - LCS 2]
# 두 문자열의 최장 공통 부분 수열(Longest Common Subsequence, LCS)의
# '길이'와 '실제 수열'을 모두 출력하는 문제.
# 핵심은 DP의 대표 패턴: "대각선 + 1 / 위 또는 왼쪽 중 큰 값" 전이 구조.

# 1. 입력 받기
first = input().strip()
second = input().strip()

# 2. DP 테이블 초기화
# dp[i][j] = first 문자열의 앞 i개와, second 문자열의 앞 j개를 비교했을 때의 LCS "길이"
# 길이 N, M 문자열을 비교할 때, dp는 (N+1) x (M+1) 크기로 잡는다.
#   이유: dp[0][*], dp[*][0] = "아무 문자도 고려하지 않은 상태" = 0으로 시작하기 위해 --> LCS, 편집거리 같은 문제에서는.. 공집합 고려
dp = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]

# 3. DP 전이 수행
# 전이식의 논리:
#   - 문자가 같을 때:  대각선 값(dp[i-1][j-1]) + 1
#   - 문자가 다를 때:  위쪽(dp[i-1][j])과 왼쪽(dp[i][j-1]) 중 큰 값
#   - 즉, LCS는 "마지막 문자가 같다면 대각선 누적 / 다르면 큰 쪽 유지"

for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        # 문자열은 0-index이므로 실제 비교는 i-1, j-1 인덱스로 해야 함
        if first[i - 1] == second[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# (참고)
# dp 테이블의 오른쪽 아래 (dp[len(first)][len(second)])에는
# 두 문자열 전체를 비교했을 때의 LCS 길이가 저장됨.

# 4. LCS 문자열 역추적 (Backtracking)
# DP를 채우고 난 뒤, 실제 LCS 문자열을 찾기 위해 뒤에서부터 역으로 추적한다.
# 원리:
#   - dp[i][j]에서 왼쪽(dp[i][j-1])과 위쪽(dp[i-1][j]) 중
#     현재 값과 같은 곳으로 이동 → 해당 문자는 LCS에 포함되지 않음
#   - 만약 first[i-1] == second[j-1]라면,
#     해당 문자는 LCS에 포함되므로 결과에 추가하고 대각선 방향으로 이동.

i, j = len(first), len(second)
lcs = []  # 실제 LCS 문자열을 담을 스택(뒤집어서 출력 예정)

while i > 0 and j > 0:
    # case1. 두 문자가 같다면, 이 문자는 LCS의 일부
    if first[i - 1] == second[j - 1]:
        lcs.append(first[i - 1])  # 뒤에서부터 탐색하므로 나중에 뒤집어야 함
        i -= 1
        j -= 1
    # case2. 위쪽이 더 크면 위로 이동
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    # case3. 왼쪽이 더 크거나 같으면 왼쪽으로 이동
    else:
        j -= 1

# 5. 결과 출력
# LCS 길이 = dp의 마지막 값
# LCS 문자열 = 역추적 결과를 뒤집어서 출력
print(dp[-1][-1])
print(''.join(reversed(lcs)))