# DDR(Dance Dance Revolution)
'''
    [풀이과정]
    우선, 지시사함의 길이가 10만 --> 절대 완전탐색은 불가능
    그러면.. 내가 지금 당장 머릿속에 떠오른 방법은 2가지 --> DP or 그리디
    그런데.. 그리디를 쓰려면 모든 상태가 독립적인지 확인해 봐야 하는데, 그건 아니다
    그러면.. 바로 DP로 선회해야 할 것 같다.
    --> 각 커맨드 하나씩 순회하면서..
        dp 테이블을 채워 나가면 되지 않을까 하는 생각이 든다
    --> dp[n][i][j] -> n번째 지시사항을 수행했을 때, 왼발이 i, 오른발이 j에 있을 때, 현재까지 든 최소 힘
    --> 그러면, 전이식은 어떻게 세워야 할까?
'''

# 지시사항 입력받기
orders = list(map(int, input().split()))
orders.pop()  # 마지막 0 제거

# DP 배열 초기화
INF = float('inf')
dp = [[[INF] * 5 for _ in range(5)] for _ in range(len(orders) + 1)]
dp[0][0][0] = 0  # 시작 시 왼발/오른발이 중앙(0)에 있음

# 이동 비용 계산 함수
def move_cost(a, b):
    # 복잡한 조건 분리
    # ----------------------------------------------------
    # a: 현재 발 위치, b: 이동할 발판 번호
    # (1) 같은 발판으로 이동 → 1
    # (2) 중앙(0) → 다른 발판 → 2
    # (3) 반대편 → 4
    # (4) 인접한 방향 → 3
    # ----------------------------------------------------
    if a == b:
        return 1
    if a == 0:
        return 2
    if abs(a - b) == 2:
        return 4
    return 3


# 점화식 구현
# --------------------------------------------
# dp[n][l][r] = n번째 지시를 수행했을 때,
#                왼발이 l, 오른발이 r 위치에 있을 때의 최소 힘
# 전이식:
#   - 이전 상태에서 왼발을 움직인 경우
#   - 이전 상태에서 오른발을 움직인 경우
# --------------------------------------------

for i in range(len(orders)):  # 각 지시 순회
    target = orders[i] # 현재 가야 할 target 불러오기
    for l in range(5):
        for r in range(5):
            if dp[i][l][r] == INF:
                continue

            # Case 1. 왼발을 움직여 target 밟기
            new_cost = dp[i][l][r] + move_cost(l, target)
            if new_cost < dp[i+1][target][r]:
                dp[i+1][target][r] = new_cost

            # Case 2. 오른발을 움직여 target 밟기
            new_cost = dp[i][l][r] + move_cost(r, target)
            if new_cost < dp[i+1][l][target]:
                dp[i+1][l][target] = new_cost


# 결과 해석 및 검증
# --------------------------------------------
# 최종적으로 len(orders)번째까지 수행했을 때의
# dp[len(orders)][l][r] 중 최소값이 정답이다.
# --------------------------------------------

ans = INF
for l in range(5):
    for r in range(5):
        ans = min(ans, dp[len(orders)][l][r])

print(ans)

# 핵심 패턴 정리:
# 1) 상태 정의: dp[step][left][right]
# 2) 선택 정의: 왼발을 움직이거나 / 오른발을 움직이거나
# 3) 전이식: dp[next][new_left][right] / dp[next][left][new_right]
# 4) 비용 함수 분리: move_cost(a, b)
# 5) 최종 최소값 탐색