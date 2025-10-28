# 줄 세우기
'''
    [풀이과정]
    -> 일부 학생들만의 키를 비교해서, 비교한 결과를 가지고.. 줄을 세우는 프로그램?
    --> "순서대로" 출력하고, 답이 여러개면 아무거나 출력하기?
    --> 와... 이거 완전 "위상정렬"의 냄새가 팍팍 난다
'''
from collections import deque

# 키를 비교한 횟수 m, 학생 수 n
n, m = map(int, input().split())
indegree = [0 for i in range(n+1)]
graph = [[] for _ in range(n+1)]

# 키를 비교한 두 학생의 번호 입력 받기 --> 하면서 indegree 테이블 갱신
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상 정렬 수행
def topology_sort():
    q = deque()
    for i in range(1, n+1): # indegree 돌아 다니면서, indegree 0인 거 queue에 넣기
        if indegree[i] == 0:
            q.append(i)

    while q:
        v = q.popleft()
        print(v, end=' ')
        for s in graph[v]: # 연결된 애들 확인
            indegree[s] -= 1
            if indegree[s] == 0: # 갱신하니까, 얘도 indegree가 0이 되었다면
                q.append(s)

topology_sort() # 위상 정렬 수행 -> 이것 자체가 "줄을 세운 결과"를 출력한다