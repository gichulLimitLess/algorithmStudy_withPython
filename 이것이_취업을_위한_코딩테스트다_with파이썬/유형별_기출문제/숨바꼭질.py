# 숨바꼭질
# 1번 헛간으로부터 다른 모든 노드로의 최단 경로 구해야 함 -> Dijkstra가 제격?
import heapq
from collections import Counter

INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)] # 노드 개수 n만큼 배열 사이즈 책정
distance = [INF for _ in range(n+1)]

for _ in range(m): # edge의 갯수만큼 반복
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = []
heapq.heappush(q, (0, 1)) # (거리, 노드 번호) 순으로 저장
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: # 이미 방문했다고 판단되면 (-> 이미 최소값이 찍혀 있다면)
        continue

    for v in graph[now]:
        new_dist = dist + 1
        if new_dist < distance[v]: # 최소값이 갱신 되어야 한다면
            distance[v] = new_dist
            heapq.heappush(q, (new_dist, v))

# max_val = 0
# firstIdx = -1
# for i in range(1, n+1): # O(2만)
#     if distance[i] != INF: # 방문 못하는 애들 아닐 때만, max_val 갱신해야 함
#        max_val = max(max_val, distance[i])
#
# firstIdx = distance.index(max_val) # 가장 작은 헛간 번호 저장
#
# # 해당하는 max_val의 갯수도 세야 함 -> O(2만)
# c1 = Counter(distance)
# count = c1[max_val]
#
# # 결과들 출력
# print(firstIdx, end=' ')
# print(max_val, end=' ')
# print(count, end=' ')

# 위처럼 해도 되긴 하는데.. 조금 더 좋은 로직으로 해보면..
max_node = 0 # 최단 거리가 가장 먼 노드 번호 (동빈이가 숨을 헛간의 번호)
max_distance = 0 # 도달할 수 있는 노드 중에서, 최단 거리가 가장 먼 노드와의 최단 거리
result = [] # 최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트

# 아래처럼 정의하면, O(2만)으로 해결 가능
for i in range(1, n+1):
    if max_distance < distance[i]: # 최댓값을 갱신해야 하는 경우라면
        max_node = i
        max_distance = distance[i]
        result = [max_node] # result 배열을 max_node만 있는 배열 하나만으로 갱신
    elif max_distance == distance[i]: # 동일한 값을 발견했다면
        result.append(i)

print(max_node, max_distance, len(result))



'''
    [참고사항]
    -> 해당 문제를 다익스트라로 풀긴 했지만, 모든 가중치가 1이므로(== 가중치가 다 똑같으므로), BFS 써도 됨!
        -> 나의 예상이 틀리지 않았군! (잘했다.... / 더 열공하자~)
'''