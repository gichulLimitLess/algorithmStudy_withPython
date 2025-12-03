# 면접보는 승범이네
'''
    [사고과정]
    - 각 면접장에 대해서, 각 도시로의 최단거리를 매번 다 구하면 안된다
        --> 현재 제약 조건에서 반드시 터지는 구조
    - 그러면 다익스트라의 동작 원리를 곰곰이 생각해 보자
        --> 다익스트라는 우선순위 큐에 현재까지의 누적 cost를 기준으로 작은 것부터 내뱉는다
        --> 자연스레, 특정 노드까지 누적된 상황에서 작은 것부터 고를려고 할 것이다
        --> 그럼 반대로..
'''
import heapq

INF = float('inf')

# 도시의 수 n / 도로의 수 m / 면접장의 수 k
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
q = []

# 도시 -> 면접장 (시간초과) / 그 반대로 간선을 연결해보자
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[v].append((u, c)) # 반대로 연결한다

# 결과를 저장할 배열 result
result = [INF for _ in range(n+1)]
interview_locs = list(map(int, input().split()))
for loc in interview_locs:
    heapq.heappush(q, (0, loc))
    result[loc] = 0

while q:
    c, now = heapq.heappop(q)
    if result[now] < c: # 이미 더 최소가 저장되어 있다면
        continue

    for nxt, cost in graph[now]:
        n_cost = cost + c
        if result[nxt] > n_cost: # 갱신해야 한다면
            heapq.heappush(q, (n_cost, nxt))
            result[nxt] = n_cost

# 결과 출력
city_num = max(result[1:])
print(result.index(city_num)) # 거리가 가장 먼 도시의 번호 출력
print(city_num) # 해당 도시에서 면접장까지의 거리 출력