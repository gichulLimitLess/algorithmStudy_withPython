# 플로이드
# --> 모든 도시의 쌍에 대해서 도시 a -> b 하는데 필요한 비용 최솟값..
# --> 이거는.. 무조건 "플로이드 워셜" 알고리즘을 사용해야 함

INF = int(1e10) # 비용이 최대 10만, 버스 갯수 최대 10만, 따라서 최대 100억 -> INF 일단 100억으로 설정

n = int(input()) # 도시의 개수 n
m = int(input()) # 버스의 개수 m
dp = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if dp[a][b] <= c: # 이미 있는 값이 더 크거나 같다면
        continue
    else:
        dp[a][b] = c

# 자기 자신에게 연결되는 건 0으로 처리
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dp[i][j] = 0

for k in range(1, n+1): # 도시 번호.. 1번부터 n번까지
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(1, n+1): # 정답 출력
    for j in range(1, n+1):
        if dp[i][j] == INF: # "갈 수 없는 경우"
            print(0, end = ' ')
        else:
            print(dp[i][j], end=' ')
    print()