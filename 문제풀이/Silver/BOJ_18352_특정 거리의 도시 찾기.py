# 특정 거리의 도시 찾기
# BFS로 접근해서, BFS의 depth가 정확히 K인 도시 번호들 다 출력하면 될 듯!
from collections import deque
import sys

input = sys.stdin.readline

def BFS(start, graph, visited, k):
  queue = deque()
  queue.append((start, 0)) # (노드 번호, depth) 형태로 넣는다
  visited[start] = True # 시작 노드 방문 처리
  answer = [] # 답을 저장할 배열

  while queue: # 큐가 빌 때까지
    now, depth = queue.popleft()
    if depth == k: # 정확히 답이 k인 경우
      answer.append(now)
      continue

    for v in graph[now]: # 연결된 애들 모두 살펴본다
      if not visited[v]: # 방문하지 않았을 때만
        visited[v] = True # 방문 표시
        queue.append((v, depth+1))
  
  return answer


# 도시의 갯수 n, 도로의 갯수 m, 거리 정보 k, 출발 도시 x
n, m, k, x = map(int, input().split()) 
graph = [[] for _ in range(n+1)] # 그래프 배열 생성
visited = [False for _ in range(n+1)] # 방문 여부 확인 배열

for _ in range(m): # 도로 정보 입력받기
  a, b = map(int, input().split())
  graph[a].append(b)

answers = BFS(x, graph, visited, k)

# 없으면 -1, 있으면 answers를 한줄씩 출력
if len(answers) < 1:
  print(-1)
else:
  answers.sort() # 오름차순 정렬
  for answer in answers:
    print(answer)