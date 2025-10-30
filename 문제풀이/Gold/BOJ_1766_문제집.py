# 문제집
'''
    [사고 과정]
    - 민오가 풀 문제의 "순서"를 결정
        --> '먼저 푸는 것이 좋은 문제'가 있으면 그것부터 풀어야 한다
        ==> 이거 딱 봐도... "위상 정렬"의 냄새가 난다
    - '가능하면 쉬운 문제부터' 풀어야 한다
        --> '여러 개의 답'이 아닌, '가능하면 쉬운 문제'부터 풀도록 해야 하려면..
        --> '최소 힙'(우선순위 큐)를 써야 하려나?
    - 기존에 Queue에 넣었던 방식을, heapq에 넣는 방식으로 구현해 봐야 할 듯
    - 실제 예시들을 손으로 써서 확인했고, 이제 구현해 보자.
'''
import heapq

# 문제 수 n, 먼저 푸는 것이 좋은 문제에 대한 정보 개수 m
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def find_order():
    q = []
    for i in range(1, n+1): # 노드 모두 돌아보며, indegree가 0인 것부터 찾는다
        if indegree[i] == 0:
            # (노드 번호) 삽입
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        print(now, end=' ')
        for e in graph[now]: # 연결되어 있는 애들 indegree 하나씩 빼내기
            indegree[e] -= 1
            if indegree[e] == 0: # 새로이 indegree 0이 된 애가 있다면
                heapq.heappush(q, e)

find_order() # 답 찾으러 가기