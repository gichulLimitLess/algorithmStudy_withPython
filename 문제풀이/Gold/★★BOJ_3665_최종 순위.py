# 최종 순위
'''
    [사고 과정]
    위상 정렬을 "활용"하는 문제로 기억
    --> 순위를 정할 때, 1등을 기준으로 다른 모든 정점으로의 간선을 연결
        1등은 indegree 0, 2등은 1, 3등은 2, ... 이런 식으로
    그리고, 2가지 추가 경우에 대해서도 고려해야 한다
        ==> 확실한 순위 못 찾겠으면 '?' == 위상 정렬 도중 indegree가 0인 것이 여러 번 발생한 경우
        ==> 데이터에 일관성이 없어서 순위 못정하는 경우 == 위상 정렬 도중 indegree가 0인 경우가 중간에 없는 경우

    렛츠고
'''
from collections import deque

tc = int(input())
for _ in range(tc): # 테스트 케이스만큼 진행
    n = int(input()) # 팀의 수 n
    past_order = list(map(int, input().split())) # 작년 순위
    graph = [set() for _ in range(n+1)]
    indegree = [0 for _ in range(n + 1)]  # 위상 정렬 시에 필요한 데이터 indegree
    # 1. graph에 서로 간의 연결 관계 표시하기 --> O(500^2)
    for i in range(len(past_order)):
        now = past_order[i]
        for j in range(i+1, len(past_order)):
            graph[now].add(past_order[j])
            indegree[past_order[j]] += 1 # 화살표가 향하는 쪽에 대해서 indegree +1

    # 2. 상대적으로 등수가 바뀐 쌍(갯수는 m) 입력 받기 --> O(25000)
    m = int(input())
    for _ in range(m):
        # 상대적으로 순위가 바뀐 애들 처리 진행
        a, b = map(int, input().split())
        if b in graph[a]:  # 기존: a → b
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].add(a)
            indegree[a] += 1
        else:  # 기존: b → a
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].add(b)
            indegree[b] += 1

    # 3. 위상 정렬 수행 --> O(500 + 12만5천) => 약 O(20만)
    q = deque()
    res = [] # 결과를 저장할 배열
    for i in range(1, n+1):
        if indegree[i] == 0: # indegree가 0인 애가 있으면
            q.append(i)
    # 큐에 들어간 초기값들 기준으로 검사 한 번 진행해야 함
    if len(q) == 0:
        print("IMPOSSIBLE")
    elif len(q) >= 2:
        print("?")
    else:
        flag = '' # 플래그 값
        while q:
            now = q.popleft()
            res.append(now) # 큐에서 나오자마자 결과에 넣는다
            imsi = []
            for nxt in graph[now]: # 연결되어 있는 애들 하나씩 진행한다
                indegree[nxt] -= 1
                if indegree[nxt] == 0: # 새로이 indegree가 0이 되었다면
                    imsi.append(nxt)
            if len(imsi) >= 2: # 다음으로 나올 순위가 2개 이상인 경우 --> 확실한 등수를 못 정하는 경우
                flag = '?'
                break
            else:
                for e in imsi:
                    q.append(e)
        if len(res) != n: # 모든 요소가 들어가지 못한 거면, 둘 중 하나임
            if flag == '?': # 이거면, 확실히 답을 못찾는 경우
                print('?')
            else: # 이거면, 중간에 탐색하다가 끊긴 거임
                print("IMPOSSIBLE")
        else: # 모든 요소가 들어간 것이면, 확실한 순위가 나온거임
            for e in res:
                print(e, end=' ')