# 타임머신
'''
    [사고과정]
    벨만-포드 알고리즘을 연습하는 최적의 문제 --> 알고리즘 그대로 가져다 사용하면 됨
'''
INF = int(1e9)

n, m = map(int, input().split())
dist = [INF for _ in range(n+1)] # 거리
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c)) # (시작, 도착, 비용)

def bf(start):
    dist[start] = 0 # 시작 지점은 0으로 설정
    # --> n개의 round, m개의 간선에 대해서 수행
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            nxt = edges[j][1]
            cost = edges[j][2]
            if dist[cur] != INF and dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                if i == n-1: # 이 최솟값 갱신하는 것을.. n번째 round에서도 한다 == 음의 사이클 존재하는 거임
                    return True
    return False

negative_cycle = bf(1) # 벨만-포드 수행
if negative_cycle: # 음의 사이클이 존재한다면
    print('-1')
else: # 음의 사이클 존재 안한다면 --> 1번부터 2,3,..,n번 도시로 가는 가장 빠른 시간 출력
    for i in range(2, n+1):
        print(dist[i]) if dist[i] != INF else print(-1)