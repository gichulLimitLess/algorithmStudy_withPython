# 평범한 배낭
'''
    0-1 냅색 문제 복습
    1 <= (물건 수 n) <= 100
    1 <= (최대 무게 K) <= 10만
    1 <= (각 물건 무게 W) <= 10만
    1 <= (각 물건 가치 V) <= 1000
    ------------------------------
    dp[i][j] -> i(0<=i<=n-1)번째 물건까지 고려했을 때, 최대 무게 제한이 j일때 넣을 수 있는 최대 가치
'''
# 물품 수 n, 버틸 수 있는 무게 k
n, k = map(int, input().split())
items = [(-1, -1)] # (맨 앞에는 사용 안할 것임) --> 인덱스 맞출라고
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v)) # (아이템 무게, 가치)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# 첫번째(1번째) 물건에 대해서는 미리 채워놔야 함
for j in range(k+1):
    dp[1][j] = items[1][1] if items[1][0] <= j else 0

# dp 테이블 채우기
for i in range(2, n+1):
    for j in range(1, k+1): # 최대 무게 제한이 0일 때는 아무것도 못 넣음, 1부터 확인
        if items[i][0] > j: # i번째 물건을 담을 수 없다면
            dp[i][j] = dp[i-1][j]
        # i번째 물건을 담을 수 있는 경우는 2가지 상황을 발생시킬 수 있음
        # --> i번째 물건을 넣지 않거나, 넣거나
        else:
            dp[i][j] = max(dp[i-1][j], items[i][1] + dp[i-1][j-items[i][0]])

# 끝의 아이템까지 고려했을 때, 최대 무게 제한이 k일때 넣을 수 있는 최대 가치 출력
print(dp[n][k])