INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 갯수 및 간선의 갯수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
# 인덱스 번호를 바로 노드 번호로 쓰기 위해 n+1 * n+1 만큼의 공간 생성
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정
  a, b, c = map(int, input().split())
  graph[a][b] = c

# 점화식에 따라 Floyd-Warshall 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
  for b in range(1, n+1):
    # 도달할 수 없는 경우, 도달할 수 없다고 출력
    if graph[a][b] == INF:
      print("도달할 수 없다 이 양반아~")
    # 도달할 수 있는 경우 거리를 출력
    else:
      print(graph[a][b], end = " ")
  # 개행을 하기 위해 print() 하나 출력
  print()

# ======== 추가 사항 =========
# 위 코드의 시간 복잡도는 O(N^3)
# 다익스트라에 비해 코드를 직관적으로 이해하기 쉬움!