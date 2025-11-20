# 트리의 지름
'''
    [사고 과정]
    트리의 지름을 구해라 == 가중치 있는 트리에서, 두 노드 사이의 거리가 가장 긴 것
    (해결 못함)
    --> 이것은 인터넷을 찾아보니.. 대표적인 well-known 문제였음 (심지어 증명도 있음)
    --> DFS을 이용해서 푸는 well-known 문제
'''
import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())
    tree[p].append((c, w))
    tree[c].append((p, w))


def find(start, now): # 가장 먼 지점 찾기
    for a, cost in tree[start]:
        if visited[a] == -1: # 방문하지 않았을 때만
            visited[a] = cost + now
            find(a, visited[a])

visited = [-1]*(n+1)
visited[1] = 0
find(1, 0) # 임의의 점 x에서 가장 먼 정점 y를 찾는다 --> 여기선 root를 처음으로 설정

start = visited.index(max(visited)) # 시작점은 visited 중에서 최대로
visited = [-1]*(n+1)
visited[start] = 0
find(start, 0) # 다시 가장 먼 지점을 찾아주기 --> 이번에는 start 기준
print(max(visited))