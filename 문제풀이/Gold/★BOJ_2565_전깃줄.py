# 전깃줄
# 현재 전깃줄을 없앨 거라고 선택하는 경우, 선택하지 않는 경우..
n = int(input()) # n개 입력
wire = [tuple(map(int, input().split())) for _ in range(n)]
wire.sort() # A 전봇대 기준으로 정렬

memo = [1] * n # 1은 자기 자신을 의미

for i in range(1, n): # 현재 꺼를 기준
    for j in range(i): # 현재 꺼 기준으로, 이전 꺼 탐색
        if wire[i][1] > wire[j][1]: # 현재 꺼가 이전 꺼보다 큰 경우
            memo[i] = max(memo[i], memo[j] + 1)

print(n - max(memo))