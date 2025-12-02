# 웜홀
'''
    [사고과정]
    - 테스트 케이스 개수 tc (1 <= tc <= 5)
    - 지점의 수 n (1 <= n <= 500) / 도로 개수 m (1 <= m <= 2500) / 웜홀 개수 w (1 <= w <= 200)
    - 도로 정보는.. s,e,t (s <-> e 사이의 도로, t는 이 도로를 통해 이동하는데 걸리는 시간)
    - 웜홀 정보는.. s,e,t (s -> e 사이의 웜홀, t는 이 웜홀을 통해 줄어드는 시간)
    ===> Q. 각 테스트케이스마다 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능한지 여부 판단

    문제를 다시 정의하면..
    --> 그래프 탐색하면서, 특정 지점을 다시 방문했을 때.. 최초 방문했을 때보다 시간이 작은 경우가 있는가?
    --> 도로에서 걸리는 시간은 양수 / 웜홀 타고 간 시간은 음수로 지정
    --> 특정 지점 자체는 여러 번 방문해도 된다. 상태를 (방문한 지점, 걸린 시간)으로 정의해야 할 듯
        ==> 같은 상태 or 걸린 시간이 더 크다면 입구컷 / 무한 방문 방지를 위함
'''
# from collections import deque
# INF = float('inf')
#
# def find(graph, start):
#     # 특정 시작 지점 잡아두고, 거기로 돌아왔을 때 시간적으로 뒤로 가있는지 확인
#     q = deque()
#     visited = [INF for _ in range(len(graph))] # 여기에서 방문 표시는, 거기까지 가는데 '걸린 시간' 기록
#     q.append((start, 0))
#     visited[start] = 0
#
#     # 탐색 시작 --> O(500+2500+200)
#     while q:
#         now, t = q.popleft()
#         for v, cost in graph[now]: # 그래프 탐색
#             n_time = cost + t
#             if visited[v] > n_time: # 방문하지 않은 상태여야만 함 (그것의 기준은, 기록되어 있는 시간이 더 크거나 같은 경우)
#                 visited[v] = n_time # 방문 처리
#                 if v == start and n_time < 0: # 시작으로 돌아왔는데, 시간적으로 뒤로 가있다면
#                     return 'YES'
#                 elif v != start: # 시작지점은 계속 넣어서는 안된다
#                     q.append((v, n_time))
#
#     # 여기까지 왔는데, 탐색 실패했다면, 해당 start에 대해서는 시간적으로 뒤로 가는 경우가 없는 거임
#     return 'NO'
#
# tc = int(input()) # 테스트 케이스 개수 tc (tc는 최대 5)
# for _ in range(tc):
#     n, m, w = map(int, input().split())
#     graph = [[] for _ in range(n+1)]
#     for _ in range(m): # 도로 정보 입력
#         s, e, t = map(int, input().split())
#         # 도로는 여러개일 수 있으나, 최소가 아니라면 알아서 짤릴 것이므로 그대로 구성
#         graph[s].append((e, t))  # (끝점, 걸리는 시간)으로 원소 구성
#         graph[e].append((s, t))  # 양방향 그래프이므로, 양쪽을 연결
#
#     for _ in range(w): # 웜홀 정보 입력
#         s, e, t = map(int, input().split())
#         graph[s].append((e, -t)) # (끝점, 걸리는 시간(웜홀은 시간이 줄어듬))으로 원소 구성
#
#     ans = 'NO'
#     # 시작지점 하나씩 돌아가면서, 시간적으로 뒤로 가는 경우가 있는지 확인 --> O(500 * 3200)
#     for i in range(1, len(graph)):
#         if len(graph[i]) > 0: # 연결된 도로 or 웜홀이 있는 경우에만
#             if find(graph, i) == 'YES': # 가능한 경우가 있다면
#                 ans = 'YES'
#                 break
#             else: # 없으면, 다음 start 기준으로 찾아본다
#                 continue
#
#     print(ans) # 답 출력

# ========== (중요 사실) 그래프 문제에서 '음수 간선'이 존재한다면 Dijkstra/BFS를 생각하면 안된다 ==========
# 이럴 때 사용해야 할 것은 벨만-포드!
import sys
input = sys.stdin.readline

INF = int(1e9)

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())

    edges = []

    # 1) 도로 (양방향, cost 양수)
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    # 2) 웜홀 (단방향, cost 음수)
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    # dist를 모두 0으로 초기화
    # → 모든 노드를 출발점 후보로 본다
    dist = [0] * (n + 1)

    # Bellman-Ford main: n-1번 완화
    for i in range(n - 1):
        updated = False
        for s, e, cost in edges:
            if dist[e] > dist[s] + cost:
                dist[e] = dist[s] + cost
                updated = True
        if not updated:
            break

    # n번째 완화에서 갱신 → 음수 사이클 존재
    has_cycle = False
    for s, e, cost in edges:
        if dist[e] > dist[s] + cost:
            has_cycle = True
            break

    print("YES" if has_cycle else "NO")
