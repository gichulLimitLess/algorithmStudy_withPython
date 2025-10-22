# 특정한 최단 경로
# --> 임의로 주어진 두 정점은 반드시 통과해야 함
# ===> 1번 -> v1, v1 -> v2, v2 -> N
# 이 3가지의 최단 거리를 각각 구해도 되지 않음? 다익스트라 쓴다고 가정했을 때, 해봐야 3*O(ElogV) => O(200만 * 3) == O(600만)이라서 충분할 듯

import heapq

INF = float('inf')

n, e = map(int, input().split()) # 정점의 개수 n, 간선 개수 e
graph = [[] for _ in range(n+1)]
for _ in range(e): # 간선 정보 입력 받기
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # (연결된 노드, 거리) 정보 저장
    graph[b].append((a, c)) # 양방향이므로, 양쪽으로 저장
v1, v2 = map(int, input().split()) # 반드시 거쳐야 하는 서로 다른 정점 번호 v1, v2 주어짐

# 시작점과 끝점을 지정해 준다
def dijkstra(start, end):
    distance = [INF for _ in range(n+1)] # 모든 노드들 중 어느 노드를 거쳐 갈 지 모르기 때문에, distance는 우선 n+1만큼 크기로 선언
    q = []
    heapq.heappush(q, (0, start)) # 시작지점 heapq에 넣기
    distance[start] = 0 # 반드시 시작지점 distance 배열이 마킹해 놓기!

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 더 최소값이 있는 경우 --> 탐색 중지
            continue

        for element in graph[now]:
            cost = dist + element[1]
            if distance[element[0]] > cost: # 최소값 갱신해야 하는 경우
                distance[element[0]] = cost
                heapq.heappush(q, (cost, element[0]))

    return distance[end] # start -> end로 가는 최소 거리를 return 해준다

# 1 -> v1 -> v2 -> n
path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)

# 1 -> v2 -> v1 -> n (반대 경로도 고려해야 함)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

res = min(path1, path2)
print(res if res < INF else -1)