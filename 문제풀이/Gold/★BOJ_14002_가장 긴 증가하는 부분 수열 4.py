# 가장 긴 증가하는 부분 수열 4
'''
    [사고 과정]
    기존의 LIS 문제에다가, 백트래킹을 포함한 문제인 것 같다.
    LIS 문제는 기억해 내려다가, 실패했고..
    백트래킹 로직을 생각해 보았다.
'''
n = int(input())
n_list = list(map(int, input().split()))

# dp[i] = i번째 원소가 LIS의 마지막 원소일 때, LIS 길이 값
dp = [1 for _ in range(n)]
for idx, e in enumerate(n_list):
    max_val = 0
    for j in range(idx):
        if e > n_list[j]: # 기준점 되는 애가, 비교하고 있는 애보다 크다면
            max_val = max(max_val, dp[j])
    dp[idx] = max_val + 1

LIS_len = max(dp)
print(LIS_len) # LIS 길이 출력

# 백트래킹 시작
start = dp.index(LIS_len) # --> LIS 길이를 갖는 첫번째 인덱스 반환
cnt = LIS_len
res = []
for i in range(n-1, -1, -1):
    if dp[i] == cnt: # 현재 LIS 길이와 dp[i]의 값이 같다면.. res에 넣고, -1
        res.append(n_list[i])
        cnt -= 1

res.reverse() # 뒤집어야 제대로 된 결과다
for e in res:
    print(e, end = ' ')