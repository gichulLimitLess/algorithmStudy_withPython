# 녹색 옷 입은 애가 젤다지?
# 최단 거리를 구해야 하는데, 방향이 양방향이고, 가중치가 모두 다름 -> Dijkstra
import heapq

INF = int(1e9)

def dijkstra(board, start): # 다익스트라 수행 함수
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    # 0번에서 시작해서, n-1번까지 노드의 최단 거리 다 저장할 거임
    distance = [[INF for _ in range(n)] for _ in range(n)]
    q = []
    heapq.heappush(q, (board[start[0]][start[1]], start)) # (비용, 좌표)를 우선순위 큐에 넣기
    distance[start[0]][start[1]] = board[start[0]][start[1]] # 맨 처음은 이렇게 초기화해 주어야 한다

    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist: # 이건 볼 이유가 없음 (이미 더 작은 값이 있거든)
            continue

        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if 0 <= ny <= n-1 and 0 <= nx <= n-1: # ny, nx가 유효한 위치에 있는 동안만 수행
                cost = dist + board[ny][nx] # 연결된 곳에 갈 때의 비용 계산
                if cost < distance[ny][nx]: # 갱신할 필요가 있다면
                    distance[ny][nx] = cost
                    heapq.heappush(q, (cost, (ny, nx))) # 우선순위 큐에 넣는다

    return distance[n-1][n-1] # (0,0) -> (n-1, n-1) 까지의 최솟값 return

iter = 1 # 각 테스트 케이스의 번호
while True: # 0을 입력받을 때까지, 무한반복
    n = int(input())
    if n == 0:
        break
    else:
        board = []
        for _ in range(n): # 입력 받기
            row = list(map(int, input().split()))
            board.append(row)
        answer = dijkstra(board, (0, 0)) # 다익스트라 수행
        print(f"Problem {iter}: {answer}") # 답 answers 배열에 넣기
        iter += 1