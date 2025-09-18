# 파티
# 첫째로, 각 학생이 X로 가는 최단 경로를 구한다
# 그 다음, X에서 각 학생의 마을로 돌아가는 값들을 모두 구한다 (-> 이거 그냥 2차원 배열로 한번에 레츠고)
# 그 2개의 값을 합산했을 때, 가장 큰 친구 구하면 된다.
# ---> 시간복잡도: O(MNlogN + NlogN), 그래도 O(1억)은 안되니까 간신히 통과될 듯
import heapq
import sys

INF = int(1e9)

input = sys.stdin.readline

n, m, x = map(int, input().split()) # n, m, x 입력 받기
graph = [[] for _ in range(n+1)] # 도로 연결망 나타내는 곳
reverse_graph = [[] for _ in range(n+1)] # 역방향 그래프 만들기

for _ in range(m):
  start, end, t = map(int, input().split()) # 시작, 끝, 거리 입력받기
  graph[start].append((end, t)) # (끝점, 시간) 순서대로 저장
  reverse_graph[end].append((start, t)) # 역방향에 대해서도 저장
 
time_taken = [INF for _ in range(n+1)]
time_taken_comeback = [INF for _ in range(n+1)]

# 다익스트라 알고리즘 함수 (역방향 그래프에 대해서)
def dijkstra_reverse(start):
    q = []
    time_taken[start] = 0
    heapq.heappush(q, (0, start)) # (시간, 노드번호) 순으로 넣는다

    while q: # queue가 빌 때까지 다익스트라 계속 진행
      time, now = heapq.heappop(q) # 우선순위 큐의 맨 상단에 있는거 하나 꺼냄
      if time_taken[now] < time: # 이미 처리된 적이 있다면
        continue

      for v in reverse_graph[now]: # 연결된 애들 싹 다 넣기
        cost = time + v[1]
        if cost < time_taken[v[0]]: # 현재 노드 거쳐서, 다른 노드 가는게 더 빠를 경우
          time_taken[v[0]] = cost # 업데이트
          heapq.heappush(q, (cost, v[0])) # (시간, 노드번호) 순으로 넣는다

# 다익스트라 알고리즘 함수 (정방향 그래프에 대해서)
def dijkstra(start):
    q = []
    time_taken_comeback[start] = 0
    heapq.heappush(q, (0, start)) # (시간, 노드번호) 순으로 넣는다

    while q: # queue가 빌 때까지 다익스트라 계속 진행
      time, now = heapq.heappop(q) # 우선순위 큐의 맨 상단에 있는거 하나 꺼냄
      if time_taken_comeback[now] < time: # 이미 처리된 적이 있다면
        continue

      for v in graph[now]: # 연결된 애들 싹 다 넣기
        cost = time + v[1]
        if cost < time_taken_comeback[v[0]]: # 현재 노드 거쳐서, 다른 노드 가는게 더 빠를 경우
          time_taken_comeback[v[0]] = cost # 업데이트
          heapq.heappush(q, (cost, v[0])) # (시간, 노드번호) 순으로 넣는다
  
dijkstra_reverse(x) # 다익스트라 알고리즘 수행 (여기서.. 각 학생 -> x로 가는 비용 계산)
dijkstra(x) # 여기서.. x -> 각 학생으로 가는 비용 계산

# 이후로는, time_taken이 모두 채워졌을 것이다. 여기에서 이제 계산을 하면 된다
max_value = 0
for i in range(1, n+1):
  max_value = max(max_value, time_taken[i] + time_taken_comeback[i])

print(max_value) # 결과 출력

# --------- 오답노트 ------------
# 파이썬은 1초 제한시간 기준, 대략 O(2000만) 넘어가면... 그 알고리즘 쓰면 안되는 걸로 생각해라 걍..
# 그리고, 역방향 그래프 만들어도 비용은 똑같다는 그 발상은 겁나 신박하네...