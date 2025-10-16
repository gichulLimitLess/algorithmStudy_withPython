# 최종 순위
# 순서가 정해져 있는 무언가에서, 답을 찾아야 함 -> 이거 "위상 정렬"의 냄새가 난다
from collections import deque

tc = int(input()) # 테스트 케이스 개수

for _ in range(tc): # 테케 개수만큼 반복
    n = int(input()) # 팀의 갯수 n
    first_rank = list(map(int, input().split())) # 작년의 순위
    rank_dict = {} # 각 팀이 몇 등을 하고 있는지 저장하는 dict (-> 형태: {팀 번호: 순위})
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n)]
    for i in range(n):
        rank_dict[first_rank[i]] = i+1
        if i != 0: # 맨 첫번째만 아니라면,
            indegree[first_rank[i]] = 1
            graph[first_rank[i-1]].append(first_rank[i])

    print(rank_dict)
    m = int(input()) # 상대적으로 등수가 바뀐 쌍의 수 m
    for _ in range(m): # 바뀐 쌍에 대해 입력 받기
        a, b = map(int, input())
        # if rank_dict[a] > rank_dict[b]: # 작년 순위에 대해, a가 b보다 낮았다면 (-> 여기에서 풀이 멈춤)

'''
    [오답노트]
    (위상정렬의 3요소: graph, indegree, queue와.. 아래의 결과 3가지도 기억)
    -> 위상 정렬 수행하던 도중에.. 큐가 비면, cycle
    -> 위상 정렬 수행하던 도중에, 큐에 원소 2개 이상이면.. 위상 정렬 값이 여러 개일 수 있는 거임 == 불확정(?)
    -> 큐에 넣어야 할 노드가 1개만 있다면.. 그 노드 확정 후 간선 제거
    => 이러한 구조로 "하나의 확실한 순서만 존재하는지"를 판별할 수 있음
    
    -> 순위 그래프는 "완전 DAG"로 시작한다 / "그래프 방향성 관리/갱신" 문제였던 것..
        (-> 자기보다 순위 낮은 애들 모두를 가리키고 있는 형태)
        => 문제를 기존에 내가 생각했던 '단방향 그래프', 그리고 '정렬'로 푸는 게 아니라..
            '방향 그래프 갱신' 느낌으로 풀어야 한다!
    -> 방향을 뒤집는 연산이 잦으면, "인접 행렬"을 사용하는 게 좋다
    -> 간선을 뒤집을 땐 indegree를 양쪽에 대해 대칭 보정해야 한다.
'''