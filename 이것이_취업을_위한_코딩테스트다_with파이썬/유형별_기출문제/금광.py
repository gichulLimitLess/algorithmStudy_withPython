# 금광
# 일일이 다 탐색하려면, 답도 없다 -> dp로 풀면 좋을 듯
tc = int(input())
for _ in range(tc): # 테스트 케이스 갯수만큼 반복
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))
    dp = [[num_list[i*m+j] for j in range(m)] for i in range(n)]

    for j in range(1, m): # 열은 1부터 시작 (-> 차례차례 최댓값 계산해 나가야 하므로, 각 열 별로 봐야 함)
        for i in range(n):
            a = dp[i-1][j-1] if i-1 >= 0 else 0
            b = dp[i][j-1]
            c = dp[i+1][j-1] if i+1 < n else 0
            dp[i][j] = max(a, b, c) + dp[i][j] # 이전꺼에서 올 수 있는 3가지 경우 중 최대 + 현재 값

    max_val = 0
    for i in range(n): # 맨 마지막 열에서, 최댓값 찾기
        max_val = max(dp[i][m-1], max_val)
    print(max_val) # 최댓값 출력