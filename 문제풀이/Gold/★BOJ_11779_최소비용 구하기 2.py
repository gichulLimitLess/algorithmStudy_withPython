# 최소비용 구하기 2
# --> "출발 도시 - 도착 도시" 가는 최소 비용 및 경로 출력 / Dijkstra 레츠고

import heapq

INF = float('inf') # 무한을 나타내는 수

n = int(input()) # 도시 갯수 n (1 <= n <= 1000)
m = int(input()) # 버스 갯수 m (1 <= m <= 10만)
graph = [[] for _ in range(n+1)] # 각 도시 별 연결 정보 저장을 위한 graph
distance = [INF for _ in range(n+1)] # 매 순간마다의 최소 거리를 저장할 distance

path = [-1 for _ in range(n+1)] # 여기에는, 내가 여기 최적의 경로로 오기 위해.. 이전 노드 값을 저장한 것

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost)) # (끝 노드, 비용) 순으로 저장

start_city, end_city = map(int, input().split()) # 출발점, 도착점 도시번호 입력받기

path[start_city] = start_city
path[end_city] = end_city

def dijkstra(start): # 다익스트라 수행을 위한 함수
    q = []
    heapq.heappush(q, (0, start)) # 우선순위 큐에 넣기
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 우선순위 큐에서 빼내기
        if distance[now] < dist: # 이미 지나온 곳이면
            continue

        for element in graph[now]: # now와 연결된 애들 확인
            cost = dist + element[1] # now를 거쳐 지나갔을 때, 비용 계산
            if cost < distance[element[0]]: # 그것이, 기존에 저장되어 있는것보다 싸면
                distance[element[0]] = cost # 최소 거리 정보 갱신
                path[element[0]] = now # 최소로 올 수 있는 이전 노드 정보 갱신
                heapq.heappush(q, (cost, element[0]))

dijkstra(start_city) # 경로 정보 찾으러 들어가기
path_answer = []
now_city = end_city # 끝점부터 역추적
while True:
    path_answer.append(now_city)
    if now_city == start_city: # 시작지점 찾았으면
        break
    else:
        now_city = path[now_city] # 역추적 한다
path_answer.reverse()

# 답 출력
print(distance[end_city])
print(len(path_answer))
for city in path_answer:
    print(city, end=' ')