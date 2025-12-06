# 행렬 곱셈 순서
'''
    [사고과정]
    --> 대충 일일이 행렬 곱셈의 경우의 수를 다 따지려 할 경우.. 문제가 발생할 것 같다는 생각을 함
    그러면 dp로 풀어야 하는데.. 어떻게 점화식, 상태를 정의하지?
    dp[i][j] = i번째 행렬부터 j번째 행렬까지 곱했을 때의 곱셈 연산 횟수의 최솟값
    그런데, 이렇게 하면 점화식은?
    (이러다가 30분 초과, 답지를 보고 아래와 같은 풀이 흡수)
'''
n = int(input()) # 행렬의 개수 n
matrices = []
for _ in range(n):
    r, c = map(int, input().split())
    matrices.append((r, c))

# dp[i][j] = i+1번째 행렬부터 j+1번째 행렬까지 곱했을 때 곱셈 연산 횟수의 최솟값
dp = [[0 for _ in range(n)] for _ in range(n)]

# dp 배열 채워 나가기 --> 칸 하나씩 늘려가면서 누적
for l in range(1, n):
    for s in range(n): # 첫 행렬 i, 끝 행렬 i+l
        if s+l >= n: # 범위를 벗어난다면 --> 검사할 이유 없음
            continue

        dp[s][s+l] = int(1e9) # 지금 계산할 첫 행렬과 끝 행렬
        for t in range(s, s+l):
            dp[s][s+l] = min(dp[s][s+l], dp[s][t] + dp[t+1][s+l] + matrices[s][0] * matrices[t][1] * matrices[s+l][1])

print(dp[0][n-1])