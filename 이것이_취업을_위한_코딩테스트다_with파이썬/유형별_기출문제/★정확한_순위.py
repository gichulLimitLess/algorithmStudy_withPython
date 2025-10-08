# 정확한 순위
# --> 각 연결관계에 대해, 각 축에 대해.. 모두 갈 수 있다면 정확한 순위 파악 가능 / 아니면 X
INF = int(1e9)
n, m = map(int, input().split()) # 학생들의 수 n, 두 학생의 성적 비교 횟수 m
cost = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    cost[a][b] = 1 # 연결되어 있음을 표현

# 자기 자신은 거리가 0이라고 표현
for i in range(n):
    for j in range(n):
        if i == j:
            cost[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j]) # 거쳐갈 수 있는게 더 작다면, 그걸로 표현

res = 0
for k in range(1, n+1): # 1부터 n번 학생까지, 쌍이 있는지(==경로가 있는지) 확인
    cnt = 0
    for i in range(1, n+1):
        if cost[i][k] != INF or cost[k][i] != INF: # A -> B, 혹은 B -> A 가능한 경로가 하나라도 있는 경우
            cnt += 1
        else:
            continue
    if cnt == n: # 서로 오고갈 수 있는 모든 쌍이 존재하는 경우
        res += 1

print(res) # 결과 출력