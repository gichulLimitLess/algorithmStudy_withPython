# ACM Craft
'''
    ex) 4번 건물을 짓기 위해서는 2, 3번 건물이 모두 건설 완료 되어야지만 4번 건물의 건설 시작 가능
        --> 난 여기서 "위상 정렬"의 냄새를 맡았다
    위상 정렬을 진행하면서 그런데 중요한 점은, indegree가 0이 되는 경우가 한 번에 여러 개 발생하면.. 답이 여러 개일수 있다는 것이다.
    이러한 점을 유의할 때, 특정 건물을 가장 빨리 지을 때까지 걸리는 최소 시간을 구하려면.. 시간을 "누적"하는 테크닉이 필요할 것 같다.
    누적하는 테이블(total_times)를 만들어서, 이전 꺼를 모두 마쳤을 때의 최소 시간으로 계속해서 누적해야 나가야 한다. (max() 사용해야 할 듯?)
    => 위상 정렬을 시간 복잡도가 O(V+E)이므로, 그리고 total_times 아무리 길어봤자 1000이므로 시간초과/메모리초과 절대 안날 듯?
'''
from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)

t = int(input())
for _ in range(t): # 테스트 케이스만큼 반복
    n, k = map(int, input().split()) # 건물 개수 n, 건설순서 규칙 k
    input_times = list(map(int, input().split()))
    build_times = [0 for _ in range(n+1)] # 각 건물 당 건설에 걸리는 시간
    total_times = [0 for _ in range(n+1)] # 각 건물을 짓기 위한 총 시간 (최소 값들만 저장할 것임)

    for i in range(1, n+1):
        build_times[i] = input_times[i-1]

    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    for _ in range(k): # 건설 순서 입력 받기
        x, y = map(int, input().split())
        graph[x].append(y) # 건물 x를 지은 다음에 건물 y를 짓는 것이 가능하다
        indegree[y] += 1

    w = int(input()) # 승리하기 위해 건설해야 할 건물 번호 w

    q = deque()
    for i in range(1, n+1): # indegree 훑어 가면서 값이 0인 곳 확인
        if indegree[i] == 0:
            q.append(i) # queue에 먼저 집어 넣는다
            total_times[i] = build_times[i] # 총 걸리는 시간에 대해서도 일단 초기화해 놓는다

    while q: # 큐가 빌 때까지 반복
        now = q.popleft()
        if now == w: # 건설해야 할 건물 번호 w 찾았으면
            print(total_times[now])
            break

        for v in graph[now]: # 연결되어 있는 애들 탐색
            indegree[v] -= 1
            total_times[v] = max(total_times[v], total_times[now] + build_times[v]) # 둘 중 더 큰 값으로 total_times를 채워야 한다
            if indegree[v] == 0: # 0이 되었다면..
                q.append(v)