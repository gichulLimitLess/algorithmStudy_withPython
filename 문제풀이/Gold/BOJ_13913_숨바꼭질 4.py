# 숨바꼭질 4
'''
    전형적인 BFS + 약간의 백트래킹 응용
    백트래킹용 배열과 방문 처리용 배열을 따로 만들어 놓는 건 어떨까?
    --> 그 칸을 가는데 걸린 시간: visited_time
    --> 그 칸을 가기 '직전'의 칸: visited_prev
'''
from collections import deque

# 수빈이 위치 n, 동생 위치 k
n, k = map(int, input().split())
visited_time = [-1 for _ in range(100001)]
visited_prev = [-1 for _ in range(100001)]

q = deque()
q.append((n, 0)) # (위치, 걸린 시간) 삽입
visited_time[n] = 0
visited_prev[n] = -100
while q:
    loc, time = q.popleft()
    if loc == k: # 동생 찾았으면
        break # 종료

    # 앞뒤로 1씩 이동
    for i in [-1, 1]:
        n_loc = loc + i
        if 0 <= n_loc <= 100000 and visited_time[n_loc] == -1: # 범위 내이고, 방문하지 않았을 때만
            visited_time[n_loc] = time + 1
            visited_prev[n_loc] = loc # 이전 위치 저장
            q.append((n_loc, time+1))

    # 2*X 위치로 이동
    n_loc = loc * 2
    if 0 <= n_loc <= 100000 and visited_time[n_loc] == -1:  # 범위 내이고, 방문하지 않았을 때만
        visited_time[n_loc] = time + 1
        visited_prev[n_loc] = loc  # 이전 위치 저장
        q.append((n_loc, time + 1))

# 1. 수빈이가 동생을 찾는 가장 빠른 시간 출력
print(visited_time[k])
path = [k]
idx = k
while True:
    if idx == n: # 경로 다 찾았으면
        break
    path.append(visited_prev[idx])
    idx = visited_prev[idx]
path.reverse()

# 2. 어떻게 이동해야 하는지 공백으로 구분해 출력
for e in path:
    print(e, end=' ')