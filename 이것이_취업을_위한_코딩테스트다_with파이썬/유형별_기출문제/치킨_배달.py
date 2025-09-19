# 치킨 배달
# 완탐으로 풀 수 있는지 탐색 --> 충분히 풀 수 있음 (O(200만)도 안되는듯)

from itertools import combinations

INF = int(1e9)

n, m = map(int, input().split())
board = []
# board 입력 받기
for _ in range(n):
  row = list(map(int, input().split())) # 한 행 입력받기
  board.append(row)

house_location = []
chickenstore_location = []
# board를 순회하며 집 좌표, 치킨 가게 좌표 정보 입력 (O(2500))
for i in range(len(board)):
  for j in range(len(board[i])):
    if board[i][j] == 1: # 집이면
      house_location.append((i+1, j+1)) # 좌표가 1부터 시작하는 것을 유의
    elif board[i][j] == 2: # 치킨집이면
      chickenstore_location.append((i+1, j+1))

total_chicken_dist = INF # '도시의 치킨 거리' 값을 저장하고 있을 것임

# 치킨집 좌표 중에서 m개를 뽑아 조합 만들기 --> O(2000 * 2n * m)
for set in combinations(chickenstore_location, m): 
  total = 0
  for house in house_location: # 집마다, 어느 치킨집이 제일 가까운지 계산 때려야 함
    chicken_dist = INF
    for store in set: # 치킨집 하나씩 순회하며 거리 계산
      cost = abs(store[0]-house[0]) + abs(store[1]-house[1]) # 거리 계산
      chicken_dist = min(cost, chicken_dist) # 계산한 cost가 '치킨 거리'인지 확인 후 갱신
    total += chicken_dist # 구해낸 '치킨 거리'를 더한다 ('도시의 치킨 거리' 구할 때 활용)
  
  total_chicken_dist = min(total, total_chicken_dist) # '도시의 치킨 거리'가 갱신 되는지 확인

print(total_chicken_dist) # 구해낸 '도시의 치킨 거리' 구하기