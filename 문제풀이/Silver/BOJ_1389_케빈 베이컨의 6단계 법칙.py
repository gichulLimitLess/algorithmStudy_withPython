# 케빈 베이컨의 6단계 법칙
'''
    [사고과정]
    --> '플로이드-워셜'의 쉬운 버전으로 문제를 풀면 될 것 같은 생각이 든다
    --> 친구 관계가 중복되어 들어올 수 있으므로, 매번 해당 내용에 대해서, 검사를 해줘야 한다
        --> 근데, 이건 사실 set()으로 넣어 놓으면 되는 거 아님?
'''
# 유저의 수 n, 친구 관계의 수 m
INF = int(1e9)

n, m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1): # 자기 자신과의 거리는 0으로 초기화
    dist[i][i] = 0

for i in range(1, n+1): # 거리 정보가 이미 있는 애들은 이렇게 초기화
    for e in graph[i]:
        dist[i][e] = 1

# 플로이드 워셜 수행 ---> O(N^3)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

print(dist)
min_val = INF
min_user = 0
for user in range(1, n+1): # 케빈 베이컨 수가 제일 작은 사람 찾기
    now = sum(dist[user][1:]) # --> O(100*100)
    if now < min_val: # 케빈 베이컨 수가 더 작은 사람이 있다면
        min_val = now
        min_user = user
print(min_user)