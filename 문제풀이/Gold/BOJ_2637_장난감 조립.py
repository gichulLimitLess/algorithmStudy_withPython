# 장난감 조립
'''
    [사고과정]
    Q. 어떤 장난감 완제품과 그에 필요한 부품들 사이의 관계가 주어졌을 때..
        하나의 장난감 완제품을 조립하기 위해 필요한 기본 부품의 종류별 개수?
    --> 순서에 따라서 차례대로 실행되어야 하는 문제.. 그리고 그것을 응용하는 문제..
        이거.. "위상 정렬"의 확장판 문제인 듯 하다
    --> "기본 부품" 자체는.. 최초에 indegree가 0인 애들이 기본 부품들이다!!
'''
from collections import deque

n = int(input()) # 1부터 n-1까지는 기본 부품 or 중간 부품 / n은 완제품 번호
m = int(input()) # 자연수 m (3 <= m <= 100) / 유방향 간선 개수
graph = [[] for _ in range(n+1)]
cost_dict = dict() # 특정 노드로 가기 위해 필요한 기본 부품 수 저장 ({특정 부품: {기본 부품: 개수, ..}, ..)
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k)) # (기본 부품 or 중간 부품 x, 가중치(k)))
    indegree[x] += 1

q = deque()
# 기본 부품 찾기 -> 기본 부품 자체는, 최초에 indegree가 0인 애들이 "기본 부품"들임!!
# --> 완전 보수적으로 계산해도.. O(100*100*100)이 안될 것임
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i) # (노드)

while q:
    now = q.popleft()
    for nxt, cost in graph[now]: # 연결되어 있는 애들 확인
        indegree[nxt] -= 1
        # 다음을 가리키고 있는 부품이 뭐로 이뤄져 있는지 정보가 없다면
        if nxt not in cost_dict:
            cost_dict[nxt] = dict()
            # 현재 정보도 cost에 없다면.. "기본부품"에 대한 정보로 초기화 해야 하는 상태
            if now not in cost_dict:
                cost_dict[nxt][now] = cost
            else: # cost가 있다면.. 자식 dict를 돌면서, 주어진 가중치만큼 곱해서 넣어야 한다
                for basic, cnt in cost_dict[now].items():
                    cost_dict[nxt][basic] = cnt * cost
        # 정보가 있다면 --> 기존에 있는 수에 누적해 줘야 한다
        else:
            if now not in cost_dict: # now가 '기본부품'인 경우
                cost_dict[nxt][now] = cost
            else: # '기본부품' 아니라면..
                for basic, cnt in cost_dict[now].items():
                    if basic not in cost_dict[nxt]: # 없으면 만들고
                        cost_dict[nxt][basic] = cnt * cost
                    else: # 이미 있으면 누적해준다
                        cost_dict[nxt][basic] += (cnt*cost)

        # indegree가 0이 되었다면 queue애 넣어서 탐색을 이어간다
        if indegree[nxt] == 0:
            q.append(nxt)

# 완제품 정보에 대해서 순회하며 출력 --> 여기엔 '기본 부품' 정보만 누적되어 있을 것임
ans = []
for basic, cnt in cost_dict[n].items():
    ans.append((basic, cnt))
ans.sort() # 오름차순 정렬 --> O(100 * log100)
for basic, cnt in ans:
    print(basic, cnt)


# ================ 아래는 조금 더 직관적이고 정석적인 풀이법 (2차원 배열 활용) ================
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

# dp[x][b] = x를 만들기 위해 필요한 기본 부품 b의 개수
dp = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))
    indegree[X] += 1

q = deque()

# 1. 기본 부품 찾기: indegree == 0
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i][i] = 1       # 기본 부품은 자기 자신을 1개 필요로 한다

# 2. 위상정렬 + DP 누적
while q:
    now = q.popleft()

    for nxt, cost in graph[now]:
        # now의 기본 부품 정보를 nxt에 전달
        # dp에서 기본 부품 아닌 애들은 모두 0으로 표현되니까 그냥 1 ~ N+1에 대해 다 더해도 상관 X
        for b in range(1, N+1):
            dp[nxt][b] += dp[now][b] * cost

        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

# 3. 완제품(N)에 필요한 기본 부품만 출력
for b in range(1, N+1):
    if dp[N][b] > 0:
        print(b, dp[N][b])
