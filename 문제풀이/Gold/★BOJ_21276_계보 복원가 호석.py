# 계보 복원가 호석
# '''
#     [사고 과정]
#     - 석호촌에는 N(1 <= N <= 1000)명의 사람이 있음
#     - 정보가 "X Y" 형태로 M개 주어짐 (-> X의 조상 중에 Y가 있다는 것)
#     --> 정보가 '알파벳'으로 주어지기 때문에, 사전순으로 정렬한 다음에, 각각에 노드 번호를 부여해야 할 것 같음
#         이를 위해서 dict 자료형을 활용하면 좋을 듯! (그래프 자체는 숫자로, 매핑은 dict로)
#     - 가문 시조들의 이름을 출력하는 것 --> indegree가 0인 애들 찾는 것
#     - 이름의 사전순 대로 사람의 이름과 자식의 수, 그리고 사전순으로 자식들의 이름을 출력하는 것 --> 그래프 탐색 + 정렬
#         즉, 이 문제는 "위상정렬의 indegree 응용 + 그래프 탐색"인 것으로 판단됨
# '''
# import copy
# import heapq
# from collections import Counter, deque
#
# n = int(input())
# names = list(input().split())
# names.sort() # 이름들을 사전순으로 정렬
# namesToNum_dict = {} # '이름'과 '그래프 노드 번호' 매핑
# numToNames_dict = {} # '그래프 노드 번호'와 '이름' 매핑
# for i in range(n): # 그래프 0번부터 n-1번까지 매핑
#     namesToNum_dict[names[i]] = i # key: 이름 / value: 그래프 노드 번호
#     numToNames_dict[i] = names[i] # 반대 방향으로도 매핑
#
# indegree = [0 for _ in range(n)]
# graph = [[] for _ in range(n)]
#
# m = int(input())
# # 'x y' 형태로 입력이 주어짐 --> "x의 조상 중에 y가 있다는 것"
# for _ in range(m):
#     x, y = input().split()
#     graph[namesToNum_dict[y]].append(namesToNum_dict[x])
#     indegree[namesToNum_dict[x]] += 1 # x(자식)의 indegree +1
#
# # 위 과정을 통해 그래프 완성
#
# # ======= 여기서부터는 이제 결과 출력 =======
# c = Counter(indegree)
# print(c[0]) # 가문의 개수 출력
# starts = []
# # 1. indegree가 0인 애들 찾아서, 우선 시조들의 이름 출력
# for i in range(n):
#     if indegree[i] == 0: # 이름을 '사전순'으로 정렬해 놓은 상태에서, 차례대로 번호를 매겼기에, 사전순으로 알아서 출력
#         print(numToNames_dict[i], end = ' ')
#         starts.append(i)
# # 개행 ('\n')
# print()
#
# # 위상정렬을 '응용'해서, 바로 밑 자식만 찾는 기법 --> indgree를 1번 줄이고, 그게 0일 때만 결과에 저장
# def find_below(start):
#     imsi_indegree = copy.deepcopy(indegree) # indegree 사용해야 함
#     res = [] # start로부터 출발했을 때, indegree-1 하면 바로 0 되는 애들만 결과 저장\
#     q = deque()
#     for e in starts: # 위상정렬의 '시작점'들 모두 넣기
#         q.append(e)
#
#     while q:
#         v = q.popleft()
#         for e in graph[v]:
#             imsi_indegree[e] -= 1 # 연결된 애의 indegree -1
#             if imsi_indegree[e] == 0: # indgree가 0인 애가 새롭게 생겼다면
#                 if v == start: # 탐색해야 할 애라면..
#                     heapq.heappush(res, e)
#                 q.append(e)
#
#     return res # 우선순위 큐를 활용해서 순서대로 뽑았으므로, 여기에 있는 인덱스는 '사전순'으로 정렬되어 있음
#
# '''
#     2. 이름의 사전순 대로 사람의 이름과 자식의 수, 그리고 사전순으로 자식들의 이름 출력
#         numToNames 차례대로 훑으면서(이름의 사전 순대로 사람 이름 출력)
#         그 사람의 이름과 그 사람의 자식 수(그래프 탐색하며 노드 개수 세기),
#         사전순으로 자식들 이름 출력(탐색한 자식들 모아뒀다가, 사전순 정렬 후 출력)
#         --> 그런데, 단순하게 DFS 하면 안된다.. 특수한 경우가 있을 수 있기에, '위상 정렬'로 탐색해야 한다
# '''
# for i in range(n): # --> 시간 복잡도: O(1000 * (3000))
#     print(numToNames_dict[i], end=' ') # 이름의 사전순 대로 사람 이름 출력
#     result = find_below(i) # 시작점은 i ==> O(1000+V+E) == O(3000)
#
#     print(len(result), end=' ') # 자식의 수 출력
#     for j in result: # result는 heapq를 이용해서 저장했으므로, 사전순으로 정렬되어 있음
#         print(numToNames_dict[j], end=' ') # 자식들의 이름을 사전순으로 출력
#
#     # 개행 ('\n')
#     print()

# 계보 복원가 호석 (정답 구조에 맞춘 복습용 코드)
from collections import deque

n = int(input())
names = list(input().split())
names.sort()  # 사전순 정렬

# 매핑
namesToNum = {names[i]: i for i in range(n)}
numToNames = {i: names[i] for i in range(n)}

# 그래프 및 indegree
graph = [[] for _ in range(n)]
parents = [[] for _ in range(n)]     # ★ 직계 판별 위해 부모도 저장
indegree = [0] * n

m = int(input())
for _ in range(m):
    x, y = input().split()
    # y → x (y는 x의 조상)
    a = namesToNum[y]
    b = namesToNum[x]

    graph[a].append(b)
    parents[b].append(a)
    indegree[b] += 1


# --------------------------------------
# STEP 1. 시조(roots) 찾기
# --------------------------------------
roots = [i for i in range(n) if indegree[i] == 0]
print(len(roots))
for r in roots:
    print(numToNames[r], end=' ')
print()


# --------------------------------------
# STEP 2. 위상정렬 1번만 수행하면서 "직계 자식" 판별
# --------------------------------------

# 직계 자식 리스트 (정답 출력용)
direct_children = [[] for _ in range(n)]

# indegree는 훼손되므로 복사본 사용
imsi_indegree = indegree[:]
q = deque()

for r in roots:
    q.append(r)

while q:
    now = q.popleft()

    for nxt in graph[now]:
        imsi_indegree[nxt] -= 1

        # nxt의 indegree가 0이 되는 "그 순간" 직계 판별 수행
        if imsi_indegree[nxt] == 0:
            # nxt의 부모 목록 중에서 indegree 감소를 직접 준 부모를 확인해야 함
            # 즉, nxt의 원래 parents 중에서,
            #  "위상정렬 상에서 가장 마지막에 0이 된 부모" = 직계 부모
            # => 위상정렬 과정에서 그 부모(now)가 nxt의 indegree를 0으로 만들었다면 직계 관계
            direct_children[now].append(nxt)

            q.append(nxt)


# --------------------------------------
# STEP 3. 출력 (기존 당신의 출력 구조 유지)
# --------------------------------------

for i in range(n):
    children = direct_children[i]
    children.sort(key=lambda x: numToNames[x])  # 이름 기준 사전순 정렬

    print(numToNames[i], end=' ')
    print(len(children), end=' ')

    for c in children:
        print(numToNames[c], end=' ')
    print()
