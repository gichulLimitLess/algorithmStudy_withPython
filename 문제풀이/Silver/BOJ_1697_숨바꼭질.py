# 숨바꼭질
'''
    전형적인 BFS 문제
    --> 방문한 상태는 다시 방문하지 않도록 방문처리 하는 것이 중요!
'''
from collections import deque

n, k = map(int, input().split())
visited = [False for _ in range(100001)] # 각 점 방문 표시 위함
q = deque()
q.append((n, 0)) # (현재 위치, 걸린 시간) 저장
visited[n] = True

while q:
    now, time = q.popleft()
    if now == k: # 동생 찾았으면
        # 시간 출력하고 빠져 나간다
        # 이게 가능한 이유는, 모든 이동의 가중치가 같기 때문
        #   ----> 그런 상황에서 BFS 특성상, 가장 먼저 부합한 값이 최소 시간임
        print(time)
        break

    for nxt in [now+1, now-1, now*2]:
        if 0 <= nxt <= 100000: # 범위 내에서만 왔다갔다 해야 함
            if not visited[nxt]: # 방문하려는 곳을 방문하지 않았을 때만
                visited[nxt] = True
                q.append((nxt, time+1))