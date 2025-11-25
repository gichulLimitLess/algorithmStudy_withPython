# 벽 부수고 이동하기 4
'''
    [사고 과정]
    해당 문제에서의 핵심은, 각 벽에 대해서 아래의 프로세스를 수행해보는 것이다.
        -> 벽을 부수고 이동할 수 있는 곳으로 변경한다.
        -> 그 위치에서 이동할 수 있는 칸의 개수를 세어본다.
    => 즉, 벽이 있는 해당 칸을 포함하여, 연결되어 있는 '0'인 칸의 개수들을 모두 세야 한다

    일단, 각 칸이 1인 모든 칸에 대해서, 매번 연결된 거를 일일이 세게 되면.. 각 칸마다 최대 100만개의 칸을 세게 되고..
    이거를 1000개의 칸에 대해서만 수행해도.. O(10억)을 넘어가게 된다. 이건 반드시 시간 초과가 난다
    그러면.. 어떻게 해야 하는가?
        '0'인 칸이 나올때마다.. 연결되어 있는 정보를 저장하고,
        다시 board를 탐색하면서
        각 '벽'에 대해서 조사할 때마다.. 사방을 탐색하고, 사방의 그룹 정보를 바탕으로(겹치는 그룹이면 누적 X, 안겹치는 것끼리만!)
        그룹 정보에 저장되어 있는 '개수'를 누적하는 방식으로..
        연결 방식을 생각해야 하니까.. '서로소 집합' 개념이 들어갈 것이다
        '서로소 집합'의 개념이 들어가면.. parent 배열(또는 dict)의 개념이 들어갈 것
        이렇게 하면, 충분히 '2초' 안에 해결 가능할 것이다
'''
from collections import deque

n, m = map(int, input().split()) # 맵의 가로 n, 맵의 세로 m
# 보드판 입력받기 ---> O(100만)
board = []
for _ in range(n):
    row = list(input())
    for idx, e in enumerate(row):
        row[idx] = int(e)
    board.append(row)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
# 1. board를 한 번 쭉 뒤지면서, board에 연결된 0끼리의 그룹 정보 파악 ---> 서로소 집합 활용(O(100만))
visited = set()
parent = dict() # 기존의 서로소 집합의 문제들과 약간 다르게, parent 관련 내용을 dict로 저장 (key로 자기 자신, value로 자신의 부모 저장)
group_cnt = dict() # key: 그 집합의 부모, value: 그 집합의 원소 개수
for i in range(n): # parent 딕셔너리 초기화 --> 초기는 자기 자신으로
    for j in range(m):
        parent[(i, j)] = (i, j)

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find_group(y, x):
    q = deque()
    visited.add((y, x))  # 우선 시작점 방문 표시
    q.append((y, x))
    cnt = 1 # 집합을 이루는 원소들의 개수를 저장할 것임
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if (ny, nx) not in visited and board[ny][nx] != 1: # 탐색하려는 곳이 벽이 아니고, 방문한 곳이 아니어야 함
                    visited.add((ny, nx))
                    cnt += 1
                    union(parent, (ny, nx), (y, x)) # 두 칸을 같은 집합에 포함시킨다
                    q.append((ny, nx))
    return cnt # 집합을 이루는 원소들의 개수를 return

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and (i, j) not in visited: # 방문하지 않은 곳이어야 하고, 빈 칸이어야 함
            group_cnt[(i, j)] = find_group(i, j)

# 2. 다시 board를 탐색하면서, 벽('1')인 애들을 발견할 때마다.. 벽의 사방을 확인
#    사방에 인접해 있는 칸이 속해있는 '집합'을 확인하면서, 같지 않은 경우에만.. '누적'해서 더한 다음
#    mod 10 + 1(자기 자신)한 값을 그 칸에 넣어주면 된다 ---> O(4*100만)
visited = set() # visited 초기화, 이제는 '1' 관점에서 board를 다시 봐야 한다
for i in range(n):
    for j in range(m):
        if (i,j) not in visited and board[i][j] == 1: # '벽(1)'을 발견했을 경우
            visited.add((i, j)) # 방문한 칸으로 추가
            checked_group = set()
            total_cnt = 0
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if board[ni][nj] == 0 and (ni, nj) not in visited and parent[(ni, nj)] not in checked_group:
                        checked_group.add(parent[(ni, nj)]) # 해당 벽에 대해서, 이미 확인한 그룹으로 체킹
                        total_cnt += group_cnt[parent[(ni, nj)]] # 해당 벽에 대해서, 이동할 수 있는 칸의 수 누적
            board[i][j] = (total_cnt+1) % 10 # (total_cnt+1) mod 10한 값을 해당 칸에 넣어주면 된다

# 결과 출력 --> O(100만)
for row in board:
    for e in row:
        print(e, end='')
    print()

'''
    ============= 참고사항 ============= 
    위처럼 풀이해도, 백준에서 메모리/시간 초과 없이 맞았습니다 판정 받긴 했는데..
    여러 풀이들 찾아보니까.. Union-find 말고.. 그냥 각 그룹에 대해서, '컴포넌트 라벨링' 해서 찾은 경우가 꽤 있더라
    물론 내 접근도 틀린 건 전혀 아닌데, 위가 좀 더 효율적이라고 해서 추가적으로 공부해 봤다.
    아래 주석 처리된 코드가, 그 '컴포넌트 라벨링'인가 뭔가 해서 최적화한 코드 
        --> 실제 계산해보니, 5배 정도 빨라지긴 함 (2276ms -> 416ms) 
'''

# import sys
# from collections import deque
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# board = [list(map(int, input().strip())) for _ in range(n)]
#
# # 각 칸이 속한 컴포넌트 ID 저장
# component_id = [[-1] * m for _ in range(n)]
# component_size = []  # id -> size 매핑
#
# dy = [0, 0, 1, -1]
# dx = [1, -1, 0, 0]
#
# # 1. BFS로 0-컴포넌트 라벨링
# cid = 0
# for y in range(n):
#     for x in range(m):
#         if board[y][x] == 0 and component_id[y][x] == -1:
#             q = deque([(y, x)])
#             component_id[y][x] = cid
#             size = 1
#
#             while q:
#                 cy, cx = q.popleft()
#                 for d in range(4):
#                     ny = cy + dy[d]
#                     nx = cx + dx[d]
#                     if 0 <= ny < n and 0 <= nx < m:
#                         if board[ny][nx] == 0 and component_id[ny][nx] == -1:
#                             component_id[ny][nx] = cid
#                             q.append((ny, nx))
#                             size += 1
#
#             component_size.append(size)
#             cid += 1
#
# # 2. 벽(1)의 사방을 확인하여 결과 계산
# result = [['0'] * m for _ in range(n)]
#
# for y in range(n):
#     for x in range(m):
#         if board[y][x] == 1:
#             seen = set()
#             total = 1  # 자기 자신 포함
#
#             for d in range(4):
#                 ny = y + dy[d]
#                 nx = x + dx[d]
#                 if 0 <= ny < n and 0 <= nx < m:
#                     if board[ny][nx] == 0:
#                         gid = component_id[ny][nx]
#                         if gid not in seen:
#                             seen.add(gid)
#                             total += component_size[gid]
#
#             result[y][x] = str(total % 10)
#
# # 3. 출력
# print('\n'.join(''.join(row) for row in result))