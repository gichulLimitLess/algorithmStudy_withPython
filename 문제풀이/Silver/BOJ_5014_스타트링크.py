# 스타트링크
'''
    전형적인 BFS 문제인 듯 하다
'''
from collections import deque

f, s, g, u, d = map(int, input().split())
visited = [False for _ in range(f+1)] # f는 최대 100만
q = deque()

def bfs():
    global f,s,g,u,d
    q.append((s, 0))
    visited[s] = True
    while q:
        now, cnt = q.popleft()
        if now == g: # g층에 갈 수 있다면
            return cnt

        for nxt in [now+u, now-d]:
            if 1 <= nxt <= f and not visited[nxt]: # 방문하지 않은 곳이어야
                visited[nxt] = True # 방문 표시한다
                q.append((nxt, cnt+1))

    return 'use the stairs' # 못 했으면, 이거 'use the stairs' 돌려주기

print(bfs()) # 결과 출력