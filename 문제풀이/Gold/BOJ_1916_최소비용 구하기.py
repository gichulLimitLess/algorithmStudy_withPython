# 최소비용 구하기
# 0.5초 안에, 출발 - 도착 하는데 드는 최소 비용..
# --> 이건, Dijkstra를 써야할 듯 하다.
import heapq

INF = int(1e10 + 1) #100억 + 1 해놓은 거임


n = int(input()) # 도시 개수 n개
m = int(input()) # 버스 개수 m개
distance = [INF for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m): # 버스 개수만큼 반복 (-> 그것이 edge임)
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost)) # (끝점, 비용)

start, end = map(int, input().split()) # 시작/끝 입력받기

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 비용 순 정렬을 위해 (비용, 노드)로 저장
    while q: # queue가 빌 때까지 반복
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 갱신한 곳이면
            continue

        for element in graph[now]: # now랑 연결되어 있는 놈들 확인
            cost = dist + element[1]
            if cost < distance[element[0]]: # distance에 저장되어 있는 애가 cost보다 큰 경우
                distance[element[0]] = cost # 바로 갱신
                heapq.heappush(q, (cost, element[0])) # 큐에 넣기

dijkstra(start) # 다익스트라 수행
print(distance[end]) # 결과 출력