# RGB 거리 2
'''
    [풀이 과정]
    - N개의 집, 그런데 집의 개수가 최대 1000개, 겹치지 않는 모든 경우의 수, 최솟값 출력...
        --> 이거, 절대 DFS로 풀면 안되겠다는 생각이 들었다.
        ---> 최소값만 구할 거면.. DP를 활용해야 할 것 같다
'''

N = int(input())
house_rgb = [list(map(int, input().split())) for _ in range(N)]

ans = E = 1e9
for i in range(3):
    dp = [[E, E, E] for _ in range(N)]  # dp가 각 R, G, B로 시작했을 때
    dp[0][i] = house_rgb[0][i]  # 처음 집 색칠
    for j in range(1, N):  # 2번째 집부터 R, G, B로 색칠했을 때 최소값 갱신
        dp[j][0] = house_rgb[j][0] + min(dp[j - 1][1], dp[j - 1][2])  #
        dp[j][1] = house_rgb[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = house_rgb[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for c in range(3):
        if i != c:  # 첫번째 집과 N번째 집이 다른 경우만 선택
            ans = min(ans, dp[-1][c])
print(ans)