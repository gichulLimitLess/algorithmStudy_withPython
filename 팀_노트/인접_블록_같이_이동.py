'''
    [카카오, 삼성에서 자주 등장하는.. "인접 블록 같이 이동" 유형]
    - 같은 팀 / 같은 번호로 연결된 블록들은 “한 덩어리(group)”로 간주한다.
    - 이동 시, 그룹 전체가 같은 방향으로 이동해야 함.
    - 이동 가능한지 확인 후, 그룹 전체를 동시에 갱신해야 함.
    - BFS로 그룹 탐색 → 이동 가능 여부 확인 → 이동 수행.
'''

from collections import deque

# ───────────────────────────────
# [공통 방향 벡터]
# 상, 하, 좌, 우 (문제에 따라 방향 순서 다를 수 있음)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# ───────────────────────────────

def bfs(y, x, board, visited, same_group_rule):
    """
    ▪️ 같은 그룹에 속하는 모든 좌표를 BFS로 탐색
    ▪️ same_group_rule: (board[ny][nx], board[y][x]) -> bool
        → 문제마다 그룹 조건이 다르기 때문에 함수로 전달받는다.
        ex) 같은 숫자, 같은 팀 ID, 색상 조건 등
    """
    n, m = len(board), len(board[0])
    q = deque([(y, x)])
    visited[y][x] = True
    group = [(y, x)]
    base_val = board[y][x]

    while q:
        cy, cx = q.popleft()
        for dir in range(4):
            ny, nx = cy + dy[dir], cx + dx[dir]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if same_group_rule(board[ny][nx], base_val):
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    group.append((ny, nx))
    return group


def can_move(board, group, dir, is_blocked):
    """
    ▪️ 그룹 전체가 이동 가능한지 확인
    ▪️ is_blocked: (board[ny][nx], board[y][x]) -> bool
        → 이동 불가 조건을 판단하는 함수 (ex. 벽, 다른 팀, 격자 밖 등)
    """
    n, m = len(board), len(board[0])
    for y, x in group:
        ny, nx = y + dy[dir], x + dx[dir]
        if not (0 <= ny < n and 0 <= nx < m):  # 범위 밖
            return False
        if (ny, nx) not in group and is_blocked(board[ny][nx], board[y][x]):
            return False
    return True


def move_group(board, group, dir):
    """
    ▪️ 그룹 전체를 한 칸 이동
    ▪️ 이동 순서 주의: 기존 위치를 먼저 비운 후 새 위치 채움
    """
    num = board[group[0][0]][group[0][1]]
    for y, x in group:
        board[y][x] = 0  # 원래 자리 비움

    new_group = []
    for y, x in group:
        ny, nx = y + dy[dir], x + dx[dir]
        board[ny][nx] = num
        new_group.append((ny, nx))

    return new_group


# ───────────────────────────────
# ✅ 예제 실행 (문제에 따라 same_group_rule / is_blocked를 바꿔 사용)
# ───────────────────────────────
def same_group_rule(a, b):
    return a == b  # 같은 숫자면 같은 그룹

def is_blocked(a, b):
    return a != 0  # 빈칸(0) 외엔 이동 불가

board = [
    [1, 1, 0, 2],
    [1, 0, 0, 2],
    [0, 0, 0, 0],
    [3, 3, 0, 0],
]

visited = [[False]*4 for _ in range(4)]

group = bfs(0, 0, board, visited, same_group_rule)
print("초기 그룹:", group)

if can_move(board, group, 3, is_blocked):  # → 방향
    group = move_group(board, group, 3)
    print("이동 후 그룹:", group)

print("이동 후 board:")
for row in board:
    print(row)

'''
    초기 그룹: [(0, 0), (0, 1), (1, 0)]
    이동 후 그룹: [(0, 1), (0, 2), (1, 1)]
    이동 후 board:
    [0, 1, 1, 2]
    [0, 1, 0, 2]
    [0, 0, 0, 0]
    [3, 3, 0, 0]
'''