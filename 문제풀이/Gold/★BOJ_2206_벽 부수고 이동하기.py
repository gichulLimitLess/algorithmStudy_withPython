# 벽 부수고 이동하기
'''
    [사고 과정]
    - 다시 푸는 문제, 빠르게 해당 문제에서 어떻게 BFS를 적용할 수 있는지 판단
    - 단순하게 매번 벽에 부딪혔을 때 일일이, 벽을 부딪힌 경우 / 안 부딪힌 경우 복잡하게 나눌 필요 없음
        --> 벽에 부딪혔을 경우, '벽을 부순 여부'를 추가해서 벽뚫을 시전하면 됨 (짜피, 벽을 1개밖에 못 부수니까)
        --> 이렇게 다 해도.. board의 모든 칸은 2번씩('벽뚫'했을 때, 안했을 때.. 2가지 상황 발생)만 방문하게 될 테니까.. 최악에도 O(1000*1000*2)임
    - 그리고 BFS 특성상.. 최단 거리로 모든 칸을 방문하는 것이 자명
      이에 연장선으로.. (N,M)에 가장 빨리 도달한 것이 '최소 경로'
'''
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(input())
    for idx, e in enumerate(row):
        row[idx] = int(e)
    board.append(row)

# 최단 경로 찾기 함수
def find_minDist():
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    visited = set() # 방문한 좌표 저장 (--> (좌표, 벽뚫 여부) 저장)
    q = deque()
    q.append((0, 0, 0, 1)) # 큐에 시작지점 및 벽뚫 여부 push
    while q:
        y, x, wall_break, cnt = q.popleft()
        if y == n-1 and x == m-1: # 도달했으면
            return cnt # '최단 거리' return 후 바로 함수 종료
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny <= n-1 and 0 <= nx <= m-1: # 경계 벗어나지 않는 범위 내에서
                if (ny, nx, wall_break) not in visited: # (ny, nx)가 아직 방문 안 한 곳일 경우에만
                    if board[ny][nx] != 1: # 가려는 곳이 벽이 아닌 경우
                        visited.add((ny, nx, wall_break)) # 방문 여부 추가
                        q.append((ny, nx, wall_break, cnt+1))
                    elif board[ny][nx] == 1 and wall_break == 0: # 벽이 있는데, 벽뚫 아직 안 한 경우
                        visited.add((ny, nx, wall_break+1))
                        q.append((ny, nx, wall_break+1, cnt+1))

    return -1 # 여기 나왔을 때까지 return 안된거면, '불가능'한 것임 --> -1 반환

print(find_minDist()) # 최단 거리 출력