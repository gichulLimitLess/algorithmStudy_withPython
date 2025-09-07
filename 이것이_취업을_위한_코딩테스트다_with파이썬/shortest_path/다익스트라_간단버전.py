import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 갯수, 간선(edge)의 갯수를 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기 
# (-> 배열의 인덱스를 노드의 번호로 사용하기 위해 n+1만큼 할당)
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
  a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 뜻
  graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작 노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  
  # 시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복
  for i in range(n-1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
    now = get_smallest_node()
    visited[now] = True
    
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우, 도달할 수 없다고 출력, 아닌 경우엔 거리 출력
  if distance[i] == INF:
    print("도달할 수 없음")
  else:
    print(distance[i])

# ======== 추가 사항 =========
# 위 코드의 시간 복잡도는 O(V^2)
# ---> O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색하고, 현재 노드와 연결된 노드를 매번 일일이 확인해야 하기 때문!
# V가 한 5000개 정도면 할만할 듯, 그런데, 10000개를 넘어가면... 위험할 듯?