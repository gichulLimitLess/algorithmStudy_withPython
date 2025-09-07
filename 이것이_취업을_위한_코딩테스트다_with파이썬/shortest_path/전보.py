# 실전 문제 2 - 전보
# N: 도시의 갯수, M: 통로의 갯수, C: 메시지를 보내고자 하는 도시
# 1 <= N <= 30,000, 1 <= M <= 200,000, 1 <= C <= N
# --> 특정 노드에서, 다른 특정 노드로의 경로를 조사해서.. 메시지 받는 데 걸리는 시간(가장 늦게 받는 도시 기준으로 구해주면 될 듯)..?
# --> 그리고.. 메시지를 받는 도시의 갯수 구하기..? 와! 이거 다익스트라 써야겠다

import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline # 빠른 입력을 위함

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)] 
distance = [INF] * (n+1)

for _ in range(m): # 통로 정보 입력 받기
  start, end, z = map(int, input().split())
  graph[start].append((end, z)) # (연결된 끝점, 거리) 정보를 주입

# 다익스트라 알고리즘을 수행하는 함수
def dijkstra(start):
  queue = []
  heapq.heappush(queue, (0, start)) # 우선순위 큐에 시작점 집어넣기
  distance[start] = 0

  while queue: # queue가 빌 때까지 반복
    dist, now = heapq.heappop(queue) # queue에는 (거리, 노드) 쌍으로 주입
    
    # 꺼낸 v에 대해서, 이미 방문한 곳(dist가 더 작은 값이 이미 distance[v]에 있다면)이라면 pass
    if distance[now] < dist:
      continue
      
    # 꺼낸 노드에 대해서, 연결된 엣지에 대해 값을 모두 계산한다, 그리고 그것을 distance에 반영한다
    for element in graph[now]:
      new_dist = dist + element[1] # graph엔 (끝점, 거리) 순으로 저장되어 있음을 유의!
      
      if distance[element[0]] > new_dist: # 새로운 최솟값이 나왔다면 -> 갱신하고 queue에도 넣는다
        heapq.heappush(queue, (new_dist, element[0]))
        distance[element[0]] = new_dist

dijkstra(c) # 다익스트라 출발

# 이제, distance에는 c로부터 각 노드까지의 최소 시간 정보가 들어있을 것이다.
# 그리고, 못 가는 곳에 대해서는 INF(==1e9)로 적혀있을 것이다.
# INF의 갯수를 세고, INF가 아닌 값들 중 가장 큰 값을 공백을 기준으로 순서대로 출력하면 될 것이다!
cnt = 0
max_val = 0
for element in distance:
  if element != INF:
    cnt += 1
    max_val = max(max_val, element)

# 메시지를 받는 도시의 총 갯수, 총 걸리는 시간 공백 구분해서 출력
# 시작 노드는 제외해야 하므로, cnt-1 출력
print(cnt-1, max_val)

# ========= 참고 사항 ==========
# 최단 거리 문제는.. 헷갈릴 땐, 그림으로 먼저 그려보는 것도 좋은 방법!
# 위에서는, graph에는 (끝점, 거리) 순으로, queue에는 (거리, 노드) 순으로 저장되어 있음을 유의하자!
# queue에 (거리, 노드) 순으로 저장하는 이유는, heapq 자체가.. 첫 번째 원소 기준으로 우선순위가 정해지기 때문!
# --> 그런데, 다익스트라에서는 거리가 짧은 순으로 먼저 뽑아야 하기 때문! 그래서, 위처럼 한거임