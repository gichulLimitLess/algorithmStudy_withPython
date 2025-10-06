# 최소 스패닝 트리 (Minimum Spanning Tree)
# --> 최소 스패닝 트리를 구하기 위해선, 크루스칼 알고리즘을 사용해야 함

import sys
sys.setrecursionlimit(100000)

def find_parent(parent, x):
    if parent[x] != x: # 부모가 자기 자신이 아니면
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b: # 일반적으로 크기가 더 작은 놈을 부모로 둔다
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split()) # 정점의 갯수 v, 간선의 갯수 e 입력 받기
edges = []
parent = [i for i in range(v+1)] # 일단 맨 처음에는 부모를 자기 자신으로 초기화

for _ in range(e): # 간선 갯수만큼 입력 받기
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # 가중치 순으로 오름차순 정렬해야 하므로, c(가중치)를 맨 앞에 둠

edges.sort() # 오름차순 정렬
total_cost = 0

for edge in edges: # edge들을 모두 훑어가며, 최소 스패닝 트리를 찾는다
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b): # 둘이 부모가 겹치지 않을때만 진행 (-> 부모가 겹치면, cycle 발생)
        union(parent, a, b)
        total_cost += cost

print(total_cost)

'''
    [유의사항]
    경로 압축(path compression)을 함에도 불구하고, 
    최초 1회는 재귀 깊이 제한을 벗어날 수 있음 / 매우 특수한 케이스에서.. (recursionError)
    -> 이럴 땐, 그냥 sys.setrecursionlimit() 해버리자..
'''