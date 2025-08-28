from collections import deque

# bfs 메소드 정의
def bfs(graph, start, visited):
  # Queue 구현을 위해 deque 라이브러리 활용
  queue = deque([start])
  visited[start] = True

  # queue가 빌 때까지 반복
  while queue:
    # queue에서 하나의 원소를 뽑아본다
    v = queue.popleft()
    print(v, end = ' ')
    
    for e in graph[v]: # 현재 뽑은 노드의 인접 노드를 모두 본다
      if not visited[e]: # 인접한 곳이 방문한 곳이 아니라면
        queue.append(e) # Queue에 넣는다
        visited[e] = True # 방문 표시

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트 -> 인접 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
      
