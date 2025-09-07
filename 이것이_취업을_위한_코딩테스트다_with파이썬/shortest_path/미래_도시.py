# 실전 문제 1 - 미래 도시
# 1 <= N, M <= 100 (N: 전체 회사 갯수, M: 경로 갯수)
# 1 <= X, K <= 100 (X: 물건 판매할 회사, K: 소개팅할 회사)

# --> 1번 회사부터 시작해서, K 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 구해야 한다..
# 다익스트라는 아니고.. 음? 이거 "플로이드-워셜" 써야겠는데?
# 플로이드-워셜 O(N^3) 걸린다는데... O(100^3) == O(100만), 시간 제한 1초면 쌉가능일 것 같은데?

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에게 가는 정보는 0으로 초기화
for i in range(n+1):
  graph[i][i] = 0

# 두 회사 간의 연결 정보를 graph에 집어 넣기 (간선의 갯수만큼 레츠고)
for _ in range(m):
  a, b = map(int, input().split())
  # 양방향 그래프이니까, 반대 방향으로도 거리 정보를 넣어줘야 함
  graph[a][b] = 1
  graph[b][a] = 1

# k와 x를 입력 받기
x, k = map(int, input().split())

# 각 회사(노드)들에 대해서, 하나씩 최소 값을 갱신
for checkpoint in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][checkpoint] + graph[checkpoint][j])

# 위에서 작업하고 남은 graph는.. 각 노드에서 특정 노드로 가는 모든 최소 거리를 저장해 놓았을 것이다
# 즉, 1에서 k로 가는 최소 경로, k에서 x로 가는 최소 경로도 각 자리에 저장되어 있을 것이다
# 다시 말해, graph[1][k] + graph[k][x]가 이 문제의 정답인 것이다!
if graph[1][k] + graph[k][x] >= INF: # 못 가는 경우엔 -1 출력
  print(-1)
else:
  print(graph[1][k] + graph[k][x])

# ========= 참고 사항 ==========
# 최단 거리 문제는.. 헷갈릴 땐, 그림으로 먼저 그려보는 것도 좋은 방법!
# 답은 잘 나오고, 내가 알고리즘도 잘 세운 것 같은데 답이 자꾸 이상하게 나오면.. 내가 문제 잘 읽었는지 확인하자! (이거 풀 때, 나 x랑 k 입력 받는 거 반대로 받아서 계속 헤맸었음 ㄹㅇㅋㅋ)