# 테트로미노
'''
    [사고과정]
    - 테트로미노를 회전, 대칭하는 모든 경우의 수에 대해서 빠짐없이..
        칸 위에다가 테트로미노 대고 가능한 모든 수들의 합에 대해서 최대를 구해야 한다
        ==> 모든 경우의 수에 대해서, 수들의 합을 더하는 것은 충분히 Brute-Force 가능
    - 모든 경우의 수에 대해서 빠짐없이 계산만 하면 되는 문제
'''
# 테트로미노 관련 list 정의
# value: 공간의 왼쪽 상단 기준으로 테트로미노가 이루는 칸들의 좌표 가중치 -> (y, x) 순서
tetromino = [
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (1,0), (1,1)],

    [(0,0), (1,0), (2,0), (2,1)],
    [(0,0), (1,0), (0,1), (0,2)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(1,0), (1,1), (1,2), (0,2)],

    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (1,0), (2,0), (0,1)],
    [(0,0), (0,1), (0,2), (1,2)],

    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (1,1), (0,1), (0,2)],
    [(2,0), (1,0), (1,1), (0,1)],
    [(0,0), (0,1), (1,1), (1,2)],

    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (0,1), (1,1), (2,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)]
]

n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

max_val = 0

# t_config: 공간의 왼쪽 상단 기준으로 테트로미노가 이루는 칸들의 좌표 가중치 --> O(19 * 25000 * 4) < O(200만) / Brute-Force 가능!
for t_config in tetromino:
    # 공간의 왼쪽 상단 좌표를 (i, j)라고 설정 --> 그거 기준으로 '가중치 값(t_config)' 사용해서 테트로미노가 놓인 칸의 쓰인 수들의 합 계산
    for i in range(0, n):
        for j in range(0, m):
            total = 0
            cnt = 0
            for config in t_config: # 테트로미노가 놓인 칸에 쓰인 수들의 합 계산 --> O(4)
                ny = i + config[0]
                nx = j + config[1]
                if 0 <= ny < n and 0 <= nx < m: # 유효한 범위 내에서만 더하기
                    total += board[ny][nx]
                    cnt += 1
            if cnt == 4: # 테트로미노의 4개 칸이 모두 정상적으로 세졌을 경우에만 갱신
                max_val = max(total, max_val) # 최대 값 갱신

print(max_val) # 테트로미노가 놓인 칸에 쓰인 수들의 합의 최대값 출력


# ============ 해당 문제는 DFS로도 풀 수 있다 (아래는 그 풀이) ================
import sys
input = sys.stdin.readline

def dfs(x,y,ans,cnt):
    global maxValue

    if cnt == 4:
        maxValue = max(maxValue, ans)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            # 'ㅗ' 모양에 대해서는.. cnt가 2가 되는 순간 x,y에 대해서 dfs 돌리면.. 'ㅗ'의 회전형태가 나올 것임
            if cnt == 2:
                visited[nx][ny] = 1
                dfs(x,y,ans+data[nx][ny],cnt + 1)
                visited[nx][ny] = 0
            # 나머지 모양들은 한붓그리기가 가능하므로.. nx, ny에 대해서 계속 dfs 돌리면 될 듯
            visited[nx][ny] = 1
            dfs(nx, ny, ans + data[nx][ny], cnt + 1)
            visited[nx][ny] = 0

n,m = list(map(int,input().split()))
data = [list(map(int,input().split())) for _ in range(n)]
maxValue = 0

dx = [-1,0,0,1]
dy = [0,1,-1,0]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,data[i][j],1)
        visited[i][j] = 0

print(maxValue)