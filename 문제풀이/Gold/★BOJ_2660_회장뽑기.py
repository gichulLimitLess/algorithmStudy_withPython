# 회장 뽑기
# --> 아래는 삽질을 했던 풀이
'''
    [사고 과정]
    - 문제에서 주어진 조건을 손으로 그려봤다
        -> "회장은 회원들 중에서 점수가 가장 작은 사람이 된다" == "회장은 서로소 집합의 루트가 된다"
    - 회장 후보의 점수 == root로부터 가장 먼 친구와의 거리 (-> 이거 때문에.. path compression 여기선 쓰면 안될 것 같다)
    - 회장 후보의 수 == 서로소 집합의 개수
    - 회장 후보들 == 각 서로소 집합의 루트들
'''
# def find_parent(parent, x, depth):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x], depth+1)
#     return parent[x], depth
#
# def union(parent, a, b):
#     x = find_parent(parent, a, 1)
#     y = find_parent(parent, b, 1)
#     if x < y: # 보통 숫자가 작은 애를 부모로 올린다
#         parent[y] = x
#     else:
#         parent[x] = y
#
# n = int(input()) # 회원 수 n (1 <= n <= 50)
# parent = [i for i in range(n+1)]
# max_depth = 0
#
# while True:
#     a, b = map(int, input().split())
#     if a == -1 and b == -1:
#         break
#     else:
#         union(parent, a, b)
#
# parent_candidate = {} # ==> key: 회장 후보들의 번호, value: 회장 후보들의 점수
# # parent 배열 뒤지면서, 회장 후보들을 선출 --> O(50)
# for i in range(1, len(parent)):
#     if parent[i] == i:
#         parent_candidate[i] = 0
#
# # parent 하나씩 보면서, 각 서로소 집합의 root 까지의 최대 depth 계산 ---> O(50 * 50)
# for i in range(1, len(parent)):
#     root = find_parent(parent, i, depth)

# =============== 아래는 정답 풀이 =================
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

# 관계 입력
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

# BFS 탐색
# --> Union-Find는 "연결 여부"만 다루기 때문에.. 거리 기반 계산 하려면, BFS 해야 함
def bfs(start):
    visited = [-1] * (n+1)
    q = deque([start])
    visited[start] = 0

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
    return max(visited[1:])  # 가장 멀리 있는 사람과의 거리 --> 이게 결국 그 회원의 "점수"

scores = []
min_score = float('inf')

# --> 시간 복잡도 : O(50 * 50)
for i in range(1, n+1):
    score = bfs(i)
    scores.append(score)
    min_score = min(min_score, score) # 회장 후보를 정하려면 가장 작은 점수를 구해야 함 --> 구할 때마다 매번 최소 갱신

# 회장 후보는 최종적으로 구한 최소 점수(min_score)와 같은 점수를 가진 사람이어야 함
candidates = [i for i, s in enumerate(scores, start=1) if s == min_score]

print(min_score, len(candidates))
for candidate in candidates:
    print(candidate, end=' ')
