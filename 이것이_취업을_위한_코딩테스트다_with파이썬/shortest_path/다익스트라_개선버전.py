# heapq(우선순위 큐)를 이용해서 "최단 거리가 가장 짧은 노드"를 선택하는 과정을 훨씬 빠르게 할 수 있음!
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 갯수, 간선의 갯수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블은 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선(edge) 정보를 입력 받기
for _ in range(m):
  a, b, c = map(int, input().split())
  # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
  graph[a].append((b, c))

def dijkstra(start):
  queue = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정해서, queue에 삽입
  # (거리, 노드 번호) 쌍으로 이루어진 것을 queue에 지속적으로 삽입할 것임
  heapq.heappush(queue, (0, start))
  distance[start] = 0

  # queue가 비어있지 않다면 지속적으로 진행
  while queue:
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(queue)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 (--> 꺼낸 것이, 지금 저장되어 있는 것보다 큰 상황)
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 "최단 거리"를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우, 도달할 수 없다고 표시
  if distance[i] == INF:
    print("도달할 수 없다 이 양반아~")
  else: # 도달할 수 있는 경우 거리를 출력
    print(distance[i])

# ======== 추가 사항 =========
# 위 코드의 시간 복잡도는 O(ElogV)
# ---> E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사, O(ElogE)라 볼 수 있는데, 
# 중복 간선을 포함하지 않는다면, E는 항상 V^2보다 작음.. 
# O(ElogE) ≤ O(ElogV^2)가 된다는 것이고.. 
# O(ElogV^2) == O(2ElogV) ⇒ 간단히 O(ElogV)라고 볼 수 있음!