# 행성 연결
'''
    [사고과정]
    - 플로우를 설치하는데.. 플로우 당 관리비용: Cij --> 이게 edge의 cost
    - 행성의 수 N (1 <= N <= 1000)
    --> '제국 내 모든 행성을 연결하고, 그 유지비용을 최소화'하기 위해서는.. 크루스칼 써야 함
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

edges = []
n = int(input()) # 행성의 수 n (1 <= n <= 1000)
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if j != i: # 같지 않은 경우에만 edges에 넣기
            edges.append((row[j], i, j))

edges.sort() # 크루스칼 알고리즘 사용을 위해 오름차순 정렬
parent = [i for i in range(n)]
res = 0
for cost, a, b in edges:
    # 인접 행렬로 주어져서 양방향으로 모두 넣어놓은 경우에도, 아래에서 사이클로 잡아내기 때문에 그대로 진행하면 된다
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않을때만 진행
        union(parent, a, b)
        res += cost

print(res) # 결과 출력