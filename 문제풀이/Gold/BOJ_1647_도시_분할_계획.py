# 실전 문제 2: 도시 분할 계획 (이거 사실 백준 1647번)
# 집의 갯수 N, 길의 갯수 M (2 <= N <= 10만 / 1 <= M <= 100만)
# --> 주어진 입력에 대해서.. 2개의 "최소 신장 트리"를 만들어라 (크루스칼 알고리즘을 써야 함)
# --> 일단, 전체 정보에 관해서 1개의 "최소 신장 트리"를 만들고, 거기에서 가장 비용이 큰 경로를 짤라내면, 그게 최솟값!
import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, x, y):
  a = find_parent(parent, x)
  b = find_parent(parent, y)

  if a < b: # 더 작은 분을 부모로 올려드려야 한다
    parent[b] = a
  else:
    parent[a] = b

N, M = map(int, input().split()) # N, M 입력 받기
edges = []
parent = []

for i in range(N+1): # 최초로는.. 부모를 자기 자신으로 냅둔다
  parent.append(i)

for _ in range(M): # M개의 줄에 걸쳐 길의 정보 입력 받기
  a, b, c = map(int, input().split())
  edges.append((c, a, b)) # a번 집과 b번 집을 연결하는 길의 유지비가 c

edges.sort() # cost에 따라서 오름차순 정렬

last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
total_cost = 0

for edge in edges: # 하나씩 꺼내면서 찾는다
  cost, a, b = edge

  if find_parent(parent, a) == find_parent(parent, b): # 부모가 같다면.. (== 사이클 있다면)
    continue
  else:
    union_parent(parent, a, b)
    total_cost += cost
    last = cost # 최소 신장 트리를 구하는 크루스칼 알고리즘은.. 결국 cost를 오름차순으로 탐색하기 때문에.. 여기엔 무조건 트리 안에 있는 간선 가중치 중 가장 큰 값이 저장될 것이다

print(total_cost - last) # 이것이.. 원하는 값

# 유의사항
# --> Python에서.. 입력하는 크기가 10만을 넘어가거나 그렇다면.. input을 sys.stdin.readline으로 쓰세요