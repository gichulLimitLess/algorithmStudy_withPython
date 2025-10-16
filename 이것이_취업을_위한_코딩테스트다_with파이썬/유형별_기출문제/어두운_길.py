# 어두운 길
# --> 모든 집을 연결하긴 하는데, 최소 비용으로 연결해야 함 / 그래야 최대한 많은 금액 절약 가능
# --> 이거.. MST 만들어야 하네 / Kruskal 레츠고
def find_parent(parent, x):
    if parent[x] != x: # 부모가 자기 자신이 아니면
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b: # 더 작은 친구를 부모로 둔다
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
all_edges_cost = 0 # 모든 edge들의 비용
edges = []

parent = [i for i in range(n)] # 우선 처음에 부모는 자기 자신으로 초기화
for _ in range(m):
    x, y, z = map(int, input().split())
    all_edges_cost += z # 간선들의 총 비용을 더해 놓는다
    edges.append((z, x, y)) # (비용, x노드, y노드) 순으로 저장

edges.sort() # 비용 순으로 "오름차순" 정렬
mst_cost = 0
for z, x, y in edges: # 모든 엣지들을 살펴보며 레츠고
    if find_parent(parent, x) != find_parent(parent, y): # 사이클이 발생하지 않을 때만
        union(parent, x, y)
        mst_cost += z

print(all_edges_cost-mst_cost) # 엣지들의 총 비용에서 mst의 비용을 빼면, 그게 "절약할 수 있는 최대 금액"