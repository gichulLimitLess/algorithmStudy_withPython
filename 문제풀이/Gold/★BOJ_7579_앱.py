# 앱
'''
    [사고과정]
    - 궁극적으로 구해야 할 것은, n개의 앱들 각각에 대해 주어진 비활성화 하는데 드는 비용 ci를 보고, m 바이트 이상 확보하는 ci 합 최소를 구해야 함
    ---> 1 <= n <= 100, 1 <= m <= 1천만, 1 <= m1,..,mn <= 1천만 / 0 <= c1,..,cn <= 100, M <= m1+m2+..+mn
    - 일단, 위의 문제 조건을 보았을 때.. 단순한 완전탐색을 통해서 답을 도출하는 것은 분명히 시간 터질 것임 (2^100)
    - 그리고, M 바이트 확보하기 위해 "앱 비활성화의 최소의 비용 계산하기" --> 뭔가 Knapsack 느낌의 문제인 것 같기도 함
'''
import sys

# 정수의 개수 n과 필요한 메모리 m
n, m = map(int, sys.stdin.readline().split())

# 정수 배열
memory = [0] + list(map(int, sys.stdin.readline().split()))

# 비용 배열
cost = [0] + list(map(int, sys.stdin.readline().split()))

# DP 테이블
# 0~i 까지의 앱을 종료하거나 종료하지 않았을 때,
# j 만큼의 cost를 사용함으로써 확보 가능한 최대 메모리값
dp = [[0] * (sum(cost) + 1) for _ in range(n+1)]

# 필요한 메모리를 확보할 수 있는 최소 비용
result = int(1e9)

# DP 테이블 탐색 시작
# dp[i][j] = i번째 앱까지 고려했을 때, j 비용으로 얻을 수 있는 최대 메모리

# 아이템의 개수 + 1 만큼
for i in range(1, n+1):
    # 총 비용의 합 + 1 만큼
    for j in range(sum(cost)+1):

        # 현재 아이템의 메모리
        now_memory = memory[i]
        # 현재 아이템의 비용
        now_cost = cost[i]

        # j cost보다 현재 앱의 cost가 크다면, 아직 앱이 종료되지 않았으므로, 최대 메모리가 갱신되지 않습니다.
        if (j < cost[i]):
            dp[i][j] = dp[i-1][j]

        # j cost보다 현재 앱의 cost가 크거나 같다면, 이제 j cost로 확보 가능한 최대 메모리 값을 갱신할 수 있습니다.
        else:
            dp[i][j] = max(dp[i-1][j-now_cost] + now_memory, dp[i-1][j])

        # 현재 dp[i][j]의 값이 필요한 메모리 M 이상이 된다면
        if (dp[i][j] >= m):
            # 해당 j cost와 이전 j cost를 비교해, 더 작은 cost 값을 사용합니다.
            result = min(result, j)

print(result)