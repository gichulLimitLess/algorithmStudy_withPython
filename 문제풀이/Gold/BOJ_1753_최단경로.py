# 최단 경로
# --> 최단 경로를 구해야 하는데, 시작점 -> 다른 모든 정점으로의 최단 경로 : Dijkstra

import heapq

INF = int(1e9)

v, e = map(int, input().split()) # 정점의 갯수 v, 간선의 갯수 e
k = int(input()) # 시작 정점의 번호 k
graph = [[] for _ in range(v+1)]

for _ in range(e): # 간선 갯수만큼 반복
    a, b, w = map(int, input().split())
    graph[a].append((b,w)) # (끝점, 가중치) 저장

distance = [INF for _ in range(v+1)] # 각 정점으로의 최소 거리 저장

def dijkstra(start): # 다익스트라
    q = []
    heapq.heappush(q, (0, start)) # q에는 (가중치, 노드) 순으로 넣는다
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 더 작은 놈이 저장되어 있는 경우
            continue
        for element in graph[now]: # 연결되어 있는 놈들 탐색
            cost = dist + element[1]
            if cost < distance[element[0]]: # 최소를 갱신해야 하는 경우
                heapq.heappush(q, (cost, element[0])) # 우선순위 큐에 넣고
                distance[element[0]] = cost # 비용 갱신

dijkstra(k) # 최소 경로 찾으러 가기
for i in range(1,v+1): # i번째 줄에 i번 정점으로의 최단 경로의 경로값 출력
    if i == k:
        print(0)
    else:
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i])