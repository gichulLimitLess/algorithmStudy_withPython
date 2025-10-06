# 트리의 부모 찾기
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS 탐색
queue = deque([1])
while queue:
    node = queue.popleft()
    for child in graph[node]:
        if parent[child] == 0:  # 아직 방문 안 했다면
            parent[child] = node
            queue.append(child)

for i in range(2, n+1):
    print(parent[i])