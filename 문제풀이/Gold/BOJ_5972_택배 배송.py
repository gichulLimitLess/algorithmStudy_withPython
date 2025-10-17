# 택배 배송
# 매우 전형적인 Dijkstra 문제
# --> "가중치 다름", "최소 경로 구하기", "N,M의 갯수가 많음"
import heapq

INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost)) # (연결된 노드 번호, 비용) 순으로 저장
    graph[b].append((a, cost)) # (-> 양방향 그래프이므로, 양쪽으로 연결해 줘야 한다)

def dijkstra(): # 다익스트라 수행 함수
    distance = [INF for _ in range(n+1)]
    q = []
    heapq.heappush(q, (0, 1)) # (비용, 노드 번호) 순으로 저장 (-> 초기 출발은 1)
    distance[1] = 0 # 처음 노드 번호에 대해서, 거리 초기화
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 더 작은 값이 있다면
            continue

        for element in graph[now]: # 연결된 애들 살펴보기
            cost = element[1] + dist
            if cost < distance[element[0]]: # 최솟값 갱신해야 한다면
                distance[element[0]] = cost # 비용 갱신
                heapq.heappush(q, (cost, element[0]))

    return distance[n] # 찬홍이가 있는 헛간 n까지의 최솟값을 출력한다

print(dijkstra()) # 정답 출력