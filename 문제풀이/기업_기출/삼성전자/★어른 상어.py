# [어른 상어] - 시뮬레이션 정답 구조 (Refactored by GPT-5 x 기처리 Ver.)
# 핵심 포인트:
# - "now"와 "next" 상태를 철저히 분리해야 함
# - 각 턴마다 '이동 → 충돌 → 냄새 감소 → 냄새 추가' 순서로 동작해야 함

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# ============================
# 1️⃣ 상태 정의 (State Definition)
# ============================

# 1. 냄새 정보 [shark_num, remain_time]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]

# 2. 상어 초기 위치와 번호 기록
sharks = dict()
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] != 0:
            num = row[j]
            sharks[num] = [i, j]  # 상어의 현재 좌표 저장
            smell[i][j] = [num, k]  # 냄새 정보 초기화

# 3. 상어 초기 방향 정보 입력
dirs = list(map(int, input().split()))
shark_dir = {i+1: dirs[i]-1 for i in range(m)}

# 4. 방향 우선순위 정보 입력
#    cmd[i][d] = i번 상어가 d방향일 때의 우선순위 목록
cmd = [[] for _ in range(m+1)]
for i in range(1, m+1):
    for _ in range(4):
        row = list(map(int, input().split()))
        cmd[i].append([x-1 for x in row])

# 방향: 위, 아래, 왼쪽, 오른쪽
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# ============================
# 2️⃣ 보조 함수 정의
# ============================

def decrease_smell():
    """모든 칸의 냄새 지속 시간 1 감소 (0이면 제거)"""
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j][0] = 0  # 냄새 완전 소멸


def spread_smell():
    """각 상어가 위치한 칸에 새 냄새 남기기"""
    for num, (y, x) in sharks.items():
        smell[y][x] = [num, k]


def move_all_sharks():
    """
    모든 상어 이동 처리:
    1️⃣ 우선 '아무 냄새 없는 칸' 탐색
    2️⃣ 없으면 '자기 냄새 있는 칸' 탐색
    동시에 이동해야 하므로, next 상태를 따로 구성한다.
    """
    next_positions = dict()  # (ny, nx) → 번호 작은 상어만 생존

    for num in sorted(sharks.keys()):
        y, x = sharks[num]
        d = shark_dir[num]

        found = False

        # 1️⃣ 냄새 없는 칸 우선 탐색
        for nd in cmd[num][d]:
            ny, nx = y + dy[nd], x + dx[nd]
            if 0 <= ny < n and 0 <= nx < n and smell[ny][nx][1] == 0:
                # 이동 결정
                shark_dir[num] = nd
                found = True
                break

        # 2️⃣ 없으면 자기 냄새 칸 탐색
        if not found:
            for nd in cmd[num][d]:
                ny, nx = y + dy[nd], x + dx[nd]
                if 0 <= ny < n and 0 <= nx < n and smell[ny][nx][0] == num:
                    shark_dir[num] = nd
                    break

        # 3️⃣ 이동한 칸에 충돌 처리
        pos = (ny, nx)
        if pos not in next_positions:
            next_positions[pos] = num
        else:
            # 이미 상어가 있다면 번호가 작은 상어만 생존
            next_positions[pos] = min(next_positions[pos], num)

    # 4️⃣ 충돌 처리 후 생존 상어만 반영
    new_sharks = dict()
    for (y, x), num in next_positions.items():
        new_sharks[num] = [y, x]

    return new_sharks


# ============================
# 3️⃣ 시뮬레이션 메인 루프
# ============================

time = 0
while True:
    if len(sharks) == 1 and 1 in sharks:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break

    # ① 상어 이동
    sharks = move_all_sharks()

    # ② 냄새 감소
    decrease_smell()

    # ③ 새 냄새 남기기
    spread_smell()

    time += 1