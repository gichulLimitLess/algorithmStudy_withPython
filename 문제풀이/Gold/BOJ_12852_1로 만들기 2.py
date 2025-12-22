# 1로 만들기 2
'''
    X가 3으로 나누어 떨어지면, 3으로 나누고
    아니면 2로 나누어 떨어지면, 2로 나누고
    그래도 안되면 1을 뺀다 하는데..
    --> 어떤 경로로 오는 지에 따라서, 현재 최적이 전체 최적을 보장하지 않음 (근데, 이걸 dp로도 풀 수 있음)
        ==> 사실, 무가중치 그래프 최단거리(BFS)로 풀어볼 수도 있음
    --> 그리고, 각 단계에서 거쳐간 수들을 저장해야 함 (백트래킹)
'''
# ================== 1. DP로 풀이 ==================
# INF = int(1e9)
#
# n = int(input())
# # dp[i] = i를 만들기 위해 수행해야 하는 최소 연산 횟수
# # ---> n에서 1로 만드는 횟수를 구하는 과정이므로, "뒤에서 앞으로" 가는 게 좋을 듯
# dp = [INF for _ in range(n+1)]
# # 특정 i를 만드는 데 최소값이 어디로부터 왔는지
# parent = [-1 for _ in range(n+1)]
# dp[n] = 0 # dp[n]은 0
# for i in range(n-1, 0, -1): # --> O(100만)
#     cand1 = INF
#     cand2 = INF
#     cand3 = INF
#     # 각 상황에 대해, 유효한 범위인지 체크
#     if 1 <= i + 1 <= n:
#         cand1 = dp[i+1]+1
#     if 1 <= i * 2 <= n:
#         cand2 = dp[i*2]+1
#     if 1 <= i * 3 <= n:
#         cand3 = dp[i*3]+1
#     min_val = min(cand1, cand2, cand3)
#     if min_val == cand1: # 백트래킹을 위해, 어디로부터 왔는지 기록해 두어야 한다
#         parent[i] = i + 1
#     elif min_val == cand2:
#         parent[i] = i * 2
#     elif min_val == cand3:
#         parent[i] = i * 3
#     dp[i] = min_val # 그 중에서 최소값들을 고른다
#
# res = [1]
# now = 1
# # 백트래킹 시작
# while now < n:
#     res.append(parent[now])
#     now = parent[now]
#
# res.reverse() # 거쳐간 수의 답은 뒤집어야 한다
# print(dp[1]) # 연산을 하는 횟수의 최소값 출력
# for e in res:
#     print(e, end=' ')

# ================== 2. BFS로 풀이 ==================
from collections import deque

n = int(input())
visited = [False for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
q = deque()
q.append((n, 0))
visited[n] = True

while q:
    now, cnt = q.popleft()
    if now == 1: # queue라는 자료구조 특성상, 여기 맨 처음 온 것이 최단 거리임
        print(cnt)
        break

    # 각 상황에 대해, 유효한 범위인지 체크 --> 방문하지 않은 상태라면 바로 q에 넣기
    if 1 <= now - 1 and not visited[now - 1]:
        visited[now - 1] = True
        q.append((now-1, cnt+1))
        parent[now-1] = now # 부모 표시
    if now % 2 == 0 and 1 <= now // 2 and not visited[now // 2]:
        visited[now // 2] = True
        q.append((now//2, cnt+1))
        parent[now // 2] = now # 부모 표시
    if now % 3 == 0 and 1 <= now // 3 and not visited[now // 3]:
        visited[now // 3] = True
        q.append((now//3, cnt+1))
        parent[now // 3] = now # 부모 표시

res = [1]
now = 1
while now < n:
    res.append(parent[now])
    now = parent[now]
res.reverse() # 뒤집기 --> 거쳐온 과정은 reverse에 역순으로 저장되어 있음
for e in res:
    print(e, end=' ')