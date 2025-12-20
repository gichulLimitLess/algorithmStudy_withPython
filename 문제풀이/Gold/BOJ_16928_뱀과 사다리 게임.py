# 뱀과 사다리 게임
'''
    [사고과정]
    문제 조건을 차분히 살펴보고, 분석을 해보니, 주사위를 굴리는 각 상황에 대해서 '완전 탐색'을 진행해야 하는 BFS
    --> 특정 칸은 '재방문' 하면 안되기에, 방문 처리를 해주어야 한다
    ---> 총 시간 복잡도는 O(100)으로 매우 작을 것으로 예상
'''
from collections import deque

# 게임판에 있는 사다리 수 n, 뱀의 수 m
n, m = map(int, input().split())
visited = [False for _ in range(101)]
ladders = dict() # key로 시작점, value로 끝점
snakes = dict() # key로 시작점, value로 끝점
for _ in range(n):
    start, end = map(int, input().split())
    ladders[start] = end
for _ in range(m):
    start, end = map(int, input().split())
    snakes[start] = end

q = deque()
visited[1] = True
q.append((1, 0)) # 시작점 넣기

while q:
    now, dice_cnt = q.popleft()
    if now == 100: # 100번 칸에 먼저 도달했다면
        print(dice_cnt) # 그게 정답이며, 나가면 된다
        break
    for i in range(now+1, now+7): # 갈 수 있는 모든 곳을 탐색한다
        if 1 <= i <= 100 and not visited[i]: # 방문하지 않았을 때만
            visited[i] = True
            if i in snakes:  # '뱀'으로 연결되어 있다면
                if not visited[snakes[i]]:
                    visited[snakes[i]] = True
                    q.append((snakes[i], dice_cnt+1))
            elif i in ladders:  # '사다리'로 연결되어 있다면
                if not visited[ladders[i]]:
                    visited[ladders[i]] = True
                    q.append((ladders[i], dice_cnt+1))
            else:  # 아무것도 없는 칸이라면
                q.append((i, dice_cnt+1))  # (이동한 칸 번호, 주사위 굴린 횟수)