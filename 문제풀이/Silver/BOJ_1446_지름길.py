# 지름길
'''
    [사고과정]
    지름길 개수 N (1 <= N <= 12)
    고속도로 길이 D (1 <= N <= 10000)
    --------------------------------
    생각해보면, 그리디로 구하면 안됨
    왜냐면, 지금 0->50 가는 비용 20짜리 길이 있는데, 이걸 선택했는데,
          이후에 10->70으로 가는 비용 20짜리 길이 있었다면... 최적 구조 깨짐
    이거는, n이 12 이하이니까.. 가능한 모든 '부분집합'으로 구해야 할 듯
'''
# 지름길 개수 n, 고속도로 길이 d
# n, d = map(int, input().split())
# min_dist = d
# infos = dict()
# f_roads = []
# # now_idx: 지금 f_roads 상에서 위치, now: 지금 위치, dist: 현재까지 누적된 거리값
# def dfs(now_idx, now, dist):
#     global min_dist
#     for i in range(now_idx, len(f_roads)):
#         start, end, c = f_roads[i]
#         if start < now: # start가 now보다 작은 경우 --> 역주행
#             continue
#         if end-start > c: # 지름길 타는 조건 -> 시작, 끝 거리보다 지름길 cost가 더 작아야 함
#             dist += (start - now) # 빈 공간만큼 더해야 한다
#             dfs(i+1, end, dist+c)
#             dist -= (start - now) # 해제
#
#     # 각 dfs의 depth에서 탐색 끝나면, 여기로 내려올 것임 --> 각 단계에서 최소 거리를 갱신해줘야 함
#     dist += (d - now)
#     min_dist = min(min_dist, dist)
#
# for _ in range(n):
#     start, end, length = map(int, input().split())
#     if end > d: # 고속도로에서 역주행 불가 --> 이거는 유효하지 않은 것임
#         continue
#     # 같은 시작점, 같은 끝을 가지고 있는 길에 대해서는 최소값 1개만 있도록 유지하기 위한 조건문
#     if (start, end) not in infos or infos[(start, end)] > length:
#         infos[(start, end)] = length
#
# for key, value in infos.items():
#     f_roads.append((key[0], key[1], value)) # (시작, 끝, 거리) 삽입
#
# f_roads.sort() # 시작지점 기준으로 오름차순 정렬
# dfs(0, 0, 0) # dfs 탐색 수행
# print(min_dist) # 결과 출력

# ============= 위처럼 풀어도 충분히 좋긴 한데, dp나 다익스트라가 정석 풀이긴 함 =============
import heapq
import sys
input = sys.stdin.readline

n, d = map(int, input().split())

shortcuts = [[] for _ in range(d + 1)]
for _ in range(n):
    s, e, w = map(int, input().split())
    if e <= d and w < e - s:
        shortcuts[s].append((e, w))

INF = 10**9
dist = [INF] * (d + 1)
dist[0] = 0

pq = [(0, 0)]  # (거리, 위치)

while pq:
    cur_dist, cur = heapq.heappop(pq)
    if cur_dist > dist[cur]:
        continue

    # 기본 도로
    if cur + 1 <= d and dist[cur + 1] > cur_dist + 1:
        dist[cur + 1] = cur_dist + 1
        heapq.heappush(pq, (dist[cur + 1], cur + 1))

    # 지름길
    for nxt, cost in shortcuts[cur]:
        if dist[nxt] > cur_dist + cost:
            dist[nxt] = cur_dist + cost
            heapq.heappush(pq, (dist[nxt], nxt))

print(dist[d])
