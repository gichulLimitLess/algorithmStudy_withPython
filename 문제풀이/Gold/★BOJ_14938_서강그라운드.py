# 서강그라운드
'''
    [사고과정]
    지역의 개수 n (1 <= n <= 100)
    예은이의 수색범위 m (1 <= m <= 15), 길의 개수 r (1 <= r <= 100)
    --> Q. 수색범위 내에서 예은이가 얻을 수 있는 최대 아이템 개수?

    수색 범위 내에서.. 얻을 수 있는 최대 아이템 개수를 찾으려면..
    우선 낙하한 지점 기준으로, 각 지역(노드)으로 갈 수 있는 최단 거리를 찾아야 한다.
    --> 한 지역으로부터 다른 지역들까지의 '모든 거리'를 탐색하려면...은 플로이드-워셜!
    그런 다음, 각 지역에 있는 아이템 개수를.. 하나씩 살펴 보면서, 최단 거리가 수색 범위 m 이하면 아이템 개수를 더하면 될 듯 하다
'''
INF = int(1e9)

n, m, r = map(int, input().split())
item_cnt = [0]
item_cnt += list(map(int, input().split())) # 각 지역에 있는 아이템 개수
distance = [[INF for _ in range(n+1)] for _ in range(n+1)] # --> 이번 경우에는.. '인접 행렬'로 저장
# 자기 자신과의 거리는 0으로 초기화 --> O(10000)
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            distance[i][j] = 0

for _ in range(r): # 길 정보 입력 받기 --> O(100)
    a, b, l = map(int, input().split())
    distance[a][b] = l # (연결되어 있는 노드, 길의 길이) 저장
    distance[b][a] = l # '양방향'이므로, 반대쪽으로도 저장

# 플로이드-워셜 알고리즘 수행 --> 1부터 n번의 노드까지 (O(100^3))
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

max_itemCnt = 0
# 특정 노드로부터 출발해서, 최단 거리가 수색 범위 m 이하인 경우에 대해서, 아이템 개수를 누적해서, 최종적으로 아이템 개수의 최댓값을 찾아야 한다 --> O(10000)
for i in range(1, n+1):
    items = 0
    for j in range(1, n+1):
        if distance[i][j] <= m: # 수색 범위 안에 있을때만 아이템 획득 가능
            items += item_cnt[j]
    max_itemCnt = max(items, max_itemCnt)

print(max_itemCnt) # 정답 출력