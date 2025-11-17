# 작업
'''
    [사고과정]
    - 너무나도 전형적인 '위상정렬' 문제
        --> '선행 관계'가 존재
        --> 모든 작업을 완료하기 위해 필요한 최소 시간 구하기
    - 모든 작업을 완료하기 위한 '최소 시간'을 구하기 위해서..
        --> 선후 관계가 없는 애들끼리 중에서, '최대 시간'을 구해야 한다
'''
from collections import deque
INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n+1)]
time_info = [0 for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
total_times = [0 for _ in range(n+1)]

for i in range(1, n+1):
    info_list = list(map(int, input().split()))
    time_info[i] = info_list[0]
    for e in info_list[2:]:
        graph[e].append(i)
        indegree[i] += 1

q = deque()
# indegree가 0인 애들 우선 집어 넣기
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        total_times[i] = time_info[i] # 초기값 설정

while q: # --> O(V+E)
    now = q.popleft()
    for e in graph[now]: # 연결되어 있는 애들 indegree 감소
        indegree[e] -= 1
        total_times[e] = max(total_times[e], total_times[now] + time_info[e]) # e를 완료하는데 걸리는 시간도 최소값으로 갱신
        if indegree[e] == 0: # 새로이 0이 되었다면
            q.append(e)

print(max(total_times)) # 이게 정답임
