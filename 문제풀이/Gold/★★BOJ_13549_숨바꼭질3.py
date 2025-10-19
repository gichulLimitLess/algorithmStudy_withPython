# 숨바꼭질 3
# --> n-1, n+1, n*2, 이렇게.. 다양한 방향으로 이동할 수 있으므로, DP나 그리디 같은 거는 못 씀
# --> 이런 경우, BFS를 써보는 건 어떨까 싶다
# 각 칸에 대해, visited를 선언한다.
'''
    여기서 유의해야 할 점이 있다. 0으로 계속 순간이동 점프 했던 게 최소일 수 있는데,
    visited 찍혀있는 상태라 최소값이 제대로 갱신이 안될 수 있다.
    이 경우엔 Queue에 들어오는 순서대로 visited 처리하면 안된다.
    어떻게 하면 될까? 이 때 활용할 수 있는게 0-1 BFS
'''
from collections import deque

n, k = map(int, input().split())
# 핵심은, 각 칸에 도달했을 때의 '최소 시간'만 알면 된다
LIMIT = 100000 # --> 최대값은 100001을 넘어갈 수 없다 (모든 칸에서 1초씩 걸어갔을 때.. 1000001임)
dist = [-1] * (LIMIT+1)
q = deque()
q.append(n) # 초기 수빈이의 위치 주입
dist[n] = 0

while q: # 큐가 빌 때까지
    now = q.popleft()
    if now == k: # 수빈이를 찾았다면 --> 얘가 결국 "최단 시간" 이다 / 더 이상 탐색할 필요 X
        print(dist[now])
        break

    # 이동 가능한 모든 instruction에 대해 탐색 진행 (BFS)
    if 0 <= now * 2 <= LIMIT and dist[now*2] == -1: # 0초 걸리는 경우에 대한 것(-> 순간이동)
        dist[now*2] = dist[now]
        q.appendleft(now*2) # --> 얘는, 우선순위가 높아야 하므로, deque의 "왼쪽"에 넣는다

    for nx in (now-1, now+1): # 1초 걸리는 경우에 대한 것 (-> 앞/뒤로 이동)
        if 0 <= nx <= LIMIT and dist[nx] == -1:
            dist[nx] = dist[now]+1
            q.append(nx) # ---> 얘는, 그냥 들어오는 순서대로 처리한다