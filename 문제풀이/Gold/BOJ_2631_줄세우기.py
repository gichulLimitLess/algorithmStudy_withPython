# 줄세우기
'''
    [사고과정]
    위치를 옮길 수 있는 아이들의 수를 최소
    --> 직접 찾는 것은.. 최대 200!의 모든 경우의 수를 고려해야 함 / 그럼 DP
    --> 어..? 근데, 생각해보면, 증가하는 부분 수열 빼고 움직이면 되니까.. (증가하는 부분은 건들 필요 없음)
        "최대 길이 증가하는 부분 수열(LIS)의 길이"를 구하면, 그리고 그것을 전체 길이에서 빼면, 그게 횟수 아님?
'''
n = int(input()) # 애들 수 n
n_list = []
for _ in range(n):
    n_list.append(int(input().rstrip()))

# dp[i] -> i번째 원소를 마지막 원소로 하는 LIS의 길이
dp = [1 for _ in range(n)]
# LIS 길이 구했던 그 방식 그대로 가져오기
for i in range(1, n):
    max_val = n_list[i] # 현재 기준은 n_list에서 i번째 원소
    for j in range(i):
        if n_list[j] < max_val: # LIS의 조건을 만족하면
            dp[i] = max(dp[j] + 1, dp[i])

print(len(dp) - max(dp)) # 이게 정답임
