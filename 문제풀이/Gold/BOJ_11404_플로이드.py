# 플로이드
# --> 플로이드 워셜 알고리즘 복습 차원
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input()) # 도시의 갯수 n
m = int(input()) # 버스의 갯수 m
cost = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m): # 버스의 정보
  a, b, c = map(int, input().split())
  cost[a][b] = min(cost[a][b], c) # 우선 각각에 "최소" 비용을 저장해 둔다

# 자기 자신에게 연결되는 건 0으로 처리
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      cost[i][j] = 0

# 플로이드-워셜 알고리즘 start
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# 최종 결과 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    if cost[i][j] == INF: # 갈 수 없는 경우
      print(0, end=' ')
    else:
      print(cost[i][j], end=' ')
  print()

# --------- 유의할 점 ---------
# 문제에서.. 제한하는 제약조건이 무엇인지 확실히 확인할 필요가 있다!
# 이 문제 덕분에 플로이드-워셜 확실히 복습함 ㅎㅎ