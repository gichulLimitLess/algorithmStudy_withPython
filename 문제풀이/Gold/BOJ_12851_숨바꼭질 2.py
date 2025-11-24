# 숨바꼭질 2
'''
    [사고 과정]
    수빈이의 위치 n, 동생의 위치 k
    수빈이 위치가 x일 때 걸으면, 1초 후에 x-1 또는 x+1로 이동 / 순간이동을 하게 되면 1초 후에 2*x의 위치로 이동
    --> Q. 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인가?, 그리고 가장 빠른 시간으로 찾는 방법이 몇 가지?

    --> visited 배열을 단순히 true, false가 아니라.. 걸리는 시간을 집어 넣어놓고..
        visited 배열을 통해 판단할 때.. 현재 걸린 시간이 visited 배열에 걸린 시간보다 작거나 같다면.. 큐에 넣도록 해야 함
'''
# from collections import deque
#
# n, k = map(int, input().split())
# INF = float('inf')
# visited = [INF for _ in range(100001)] # visited 배열에는 '해당 칸까지 걸린 시간'을 저장
#
# if n == k: # 같으면.. 탐색할 필요가 없음
#     print(0)
#     print(1)
# else:
#     cnt = 0 # 가장 빠른 시간으로 찾는 '방법'의 수를 저장
#     min_time = 0
#     q = deque()
#     visited[n] = 0 # 수빈이가 있는 초기 위치는 0초 걸린다고 표시
#     if n-1 >= 0:
#         q.append((n-1, 1)) # 큐에는.. (다음 위치, 다음 위치까지 걸린 최종 시간)
#         visited[n-1] = 1
#     if n+1 <= 100000:
#         q.append((n+1, 1))
#         visited[n+1] = 1
#     if 2*n <= 100000:
#         q.append((2*n, 1))
#         visited[2*n] = 1
#
#     while q: # 큐가 빌 때까지
#         now, time = q.popleft()
#         if now == k: # 동생 찾았을 때
#             min_time = time
#             cnt += 1
#             continue # 동생 찾았으면, 이후의 과정은 queue에 안 넣어도 됨
#
#         # 다음에 갈 위치까지 걸릴 시간이, 현재 저장되어 있는 visited에 해당되는 값에서 1 뺀 것보다 작거나 같아야 함
#         if now-1 >= 0 and visited[now-1]-1 >= time:
#             q.append((now-1, time+1))
#             visited[now-1] = time+1
#         if now+1 <= 100000 and visited[now+1]-1 >= time:
#             q.append((now+1, time+1))
#             visited[now+1] = time + 1
#         if 2*now <= 100000 and visited[2*now]-1 >= time:
#             q.append((2*now, time+1))
#             visited[2*now] = time + 1
#
#     # 결과 출력
#     print(min_time)
#     print(cnt)


# ============== 위처럼 풀어도 맞긴 한데, 아래처럼 풀면 조금 더 "깔끔"하게 풀 수 있긴 함 ==========
from collections import deque

n, k = map(int, input().split())
MAX = 100000

# visited[x] = x에 도달하는 데 걸린 "최단 시간"
visited = [-1] * (MAX + 1)
# count[x] = x를 최단 시간에 도달하는 "방법의 수"
count = [0] * (MAX + 1)

# 시작 위치 초기화
queue = deque([n])
visited[n] = 0
count[n] = 1

# BFS 시작
while queue:
    x = queue.popleft()

    # 이미 최단 시간으로 k를 찾았다면
    # 그 시간보다 더 오래 걸리는 레벨은 볼 필요 없음
    if visited[k] != -1 and visited[x] > visited[k]:
        break

    # 다음 이동 후보
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= MAX:
            # 1) 첫 방문 → 최단 시간 확정
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                count[nx] = count[x]          # 경로 수 최초 배정
                queue.append(nx)

            # 2) 이미 방문한 곳인데, 동일한 최단 시간으로 도달한 경우
            elif visited[nx] == visited[x] + 1:
                count[nx] += count[x]          # 경로 수 증가

# 결과 출력
print(visited[k])
print(count[k])
