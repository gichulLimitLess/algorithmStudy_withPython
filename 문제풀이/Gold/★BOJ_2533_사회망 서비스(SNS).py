# 2533번 사회망 서비스(SNS)
# tree DP
'''
접근 방법:
DP[i][0] = i번째 노드가 서브트리의 노드고 i번째 노드가 얼리어답터가 아닐때 드는 최소 비용
DP[i][1] = i번째 노드가 서브트리의 노드고 i번째 노드가 얼리어답터 일때 드는 최소 비용
자신이 얼리 어답터가 아니면, 자신의 밑에 있는 모든 노드들은 얼리어답터여야 함.
DP[i][0] = sum(DP[below][1])
자신이 얼리 어답터라면 자식노드는 노상관
DP[i][1] = sum(min(DP[below][0], DP[below][1]))
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_020)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
DP = [[0, 0] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
def dfs(i):
    visited[i] = 1
    for below_node in tree[i]:
        if visited[below_node] == 0:
            dfs(below_node)
            DP[i][0] += DP[below_node][1]
            DP[i][1] += min(DP[below_node][0], DP[below_node][1])
    DP[i][1] += 1 # 자신이 얼리어답터라면, +1 해줘야 한다

dfs(1)
print(min(DP[1]))