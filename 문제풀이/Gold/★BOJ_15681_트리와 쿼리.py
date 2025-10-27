# 트리와 쿼리
'''
    [풀이 과정]
    - 트리를 직접 구현하려 들면, 재귀 구조.. 등의 여러 부분에서 Python의 단점이 극명히 드러남
    - 이런 경우엔, "인접 리스트"를 활용하는 게 훨씬 좋다고 하더라.
'''
import sys
# 트리의 정점 수가 최대 10^5, 그것 때문에 편향 트리이면, 최대 100000번 DFS 호출 가능
sys.setrecursionlimit(100001)

# 트리 정점 수 n / 루트 번호 r / 쿼리 수 q
n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# subTree_nodes[i] = 루트 노드가 i일 때, 서브 트리의 노드 갯수들
subTree_nodes = [i for i in range(n+1)]

# 한 번 DFS 탐색으로 서브 트리별로 노드 갯수들 모두 저장해 놔야 함
visited = {r} # 루트는 visited에 미리 넣어놓기
def make_countSubTreeNodes(node):
    subTree_nodes[node] = 1
    for v in graph[node]:
        if v not in visited: # 방문하지 않았을 때만
            visited.add(v) # 방문 표시
            subTree_nodes[node] += make_countSubTreeNodes(v)
    return subTree_nodes[node] # 이 값을 돌려준다, 이를 통해 상위 노드에서 누적해서 값을 셀 수 있도록 한다

make_countSubTreeNodes(r) # 한 번의 DFS 탐색으로 subTree_nodes 테이블 만든다

# q개의 줄에 걸쳐, 문제에 설명한 u가 하나씩 주어진다 --> O(10^5)
for _ in range(q):
    u = int(input())
    print(subTree_nodes[u]) # 한 번에 노드 갯수를 출력해야 한다
