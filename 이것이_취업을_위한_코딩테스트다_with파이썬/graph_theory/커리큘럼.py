# 실전문제 3 - 커리큘럼
# 동빈이가 듣고자 하는 강의 수: N (1 <= N <= 500)
# --> 위상 정렬을 응용하는 문제!

from collections import deque
import copy

# 노드의 갯수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
  data = list(map(int, input().split()))
  time[i] = data[0] # 첫 번째 수가 시간 정보를 담고 있음
  for x in data[1:-1]:
    indegree[i] += 1
    graph[x].append(x)

# 위상 정렬 함수
def topology_sort():
  result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
  q = deque() # 큐 기능을 사용하기 위한 deque 라이브러리 사용

  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    now = q.popleft()

    for i in graph[now]: # 그래프에서 연결된 애들에 대해 진입차수 -1씩 진행
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

# ======== 오답 노트 ==========
# 위상 정렬의 정확한 알고리즘 및 개념을 몰라서 헤맸던 문제, 위상 정렬의 개념을 제대로 다시 짚고 넘어가자!
# --> 리스트의 경우, 단순히 대입 연산을 하면 값이 변경될 때 문제가 발생할 수 있음 / 리스트 값 복제하려면 deepcopy()를 사용하자
