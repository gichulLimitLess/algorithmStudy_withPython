# 행성 터널
'''
    [사고 과정]
    - 다시 푸는 문제라서.. 어떻게 이 문제에 '크루스칼'을 적용할 수 있을지에 초점을 맞춤
    - 크루스칼 알고리즘의 본질
        -> 가장 가중치가 작은 엣지부터 하나씩 이어보며 MST를 완성하는 것
        -> 해당 엣지를 연결했을 때, 사이클이 발생하는지의 여부를 '서로소 집합'으로 탐지
    - 이번 문제에서는, 각 행성의 위치가 3차원 좌표로 주어진다
        -> 3차원 좌표로 주어지는데, 결국 각 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)
        -> 결국, x, y, z 좌표의 차 중에서, 가장 차이가 작은 좌표로 지정된다는 것인데..
        -> 이렇다는 건, x, y, z 좌표를 따로 생각해서, 각각에서 나온 가중치 따로 계산해서,
            한 곳에 모아둔 다음, 정렬 한꺼번에 시키고, 작은 것부터 채워 나가면 되는 거 아님?
            그리고, 이 엣지를 연결했을 때, 사이클이 발생하면 연결 안하고..
            그렇게 해서 풀이를 하면, 충분히 1초 안에 풀 수 있을 것 같은데?
    - x, y, z 좌표 다 따로 받아서.. 각각 좌표 배열 정렬 = 약 O(3*200만)
      각 좌표 배열 정렬한 것에서.. 엣지의 가중치 계산 = O(3*10만)
      엣지 가중치 계산한 거, 한 데 모아서 정렬 + 크루스칼 = O(30만 * log30만) = 약 O(600만)
      (크루스칼에서.. 가장 오래 걸리는 것은, 가중치별로 엣지 정렬하는 것이므로, 그것만 신경써도 됨)
    ===> 충분히 1초 안에 해결 가능할 것이라 판단
'''
import sys
input = sys.stdin.readline

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(parent, a, b):
    x = find_parent(a, parent)
    y = find_parent(b, parent)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input()) # 행성 개수 n (1 <= n <= 10만)
# x,y,z 좌표를 각각 따로 둔다
x = []
y = []
z = []
for i in range(n):
    xi, yi, zi = map(int, input().split())
    # 각 축의 좌표를 배열에 넣을 때, (각 축의 좌표, 행성 번호) 형태로 넣는다
    x.append((xi, i))
    y.append((yi, i))
    z.append((zi, i))

# x, y, z 좌표 다 따로 받아서.. 각각 좌표 배열 정렬 = 약 O(3*200만)
x.sort()
y.sort()
z.sort()
edges = []

# 각 좌표 배열 정렬한 것에서.. 엣지의 가중치 계산 = O(3*10만)
for i in range(n-1):
    # edges에는.. (가중치, 연결되어 있는 두 점) 을 넣는다
    edges.append((abs(x[i][0] - x[i+1][0]), x[i][1], x[i+1][1]))
    edges.append((abs(y[i][0] - y[i+1][0]), y[i][1], y[i+1][1]))
    edges.append((abs(z[i][0] - z[i+1][0]), z[i][1], z[i+1][1]))

# 엣지 가중치 계산한 거, 한 데 모아서 정렬 = O(30만 * log30만) = 약 O(600만)
edges.sort()
parent = [i for i in range(n)]
total = 0

# 정렬해 놓은 edges 하나씩 사이클 탐지하면서 살펴보면서, MST 완성하기
# --> '가중치' 순으로 오름차순 정렬해 놓았으므로, 무조건적으로 해당 결과는 '행성 터널의 최소 비용'을 뱉게 됨
for edge in edges:
    cost, a, b = edge
    # 부모가 겹치지 않을 때만 == 사이클이 발생하지 않을 때만
    if find_parent(a, parent) != find_parent(b, parent):
        union(parent, a, b) # 같은 집합으로 우선 합쳐주고
        total += cost

print(total) # 결과 출력