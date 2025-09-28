# 개구리의 여행
# 2025년 상반기 오전 - 2번 문제
from collections import deque

INF = int(1e9) # 10억을 넘는 결과는 나오지 않을 것이므로, INF를 무한처럼 사용

# 기본 정보 입력 받기
n = int(input()) # board의 한 줄
board = []
for _ in range(n): # board 정보 입력 받기
    row = list(input()) # 한 행 입력 받기
    board.append(row)

q = int(input()) # 여행 정보 갯수
dy = [0,0,1,-1]
dx = [1,-1,0,0]    

def can_jump(y, x, ny, nx): # 점프가 가능한지 판단하는 함수
    if ny < 0 or ny > n-1 or nx < 0 or nx > n-1: # 경계 뛰어 넘는지 검사
        return False
    if board[ny][nx] == 'S': # '미끄러운 돌'이 도착지점에 있다면
        return False
    
    if ny == y: # 이동 전/후의 y좌표가 같다면 (--> x좌표 상에서 이동한 거라면)
        if x < nx: # x가 nx보다 왼쪽에 있다면 (-> 증가하는 방향)
            for i in range(x, nx+1):
                if board[y][i] == '#': # 천적 있는 돌이 있다면
                    return False
        elif x > nx: # x가 nx보다 오른쪽에 있다면 (-> 감소하는 방향)
            for i in range(x, nx-1, -1): # x축 상에.. 천적이 있는지 검사
                if board[y][i] == '#': # 천적 있는 돌이 있다면
                    return False
    elif nx == x: # 이동 전/후의 x좌표가 같다면 (--> y좌표 상에서 이동한 거라면)
        if y < ny: # y가 ny보다 윗쪽에 있다면.. (-> 증가하는 방향) 
            for i in range(y, ny+1): # y축 상에.. 천적이 있는지 검사
                if board[i][x] == '#':
                    return False
        elif y > ny: # y가 ny보다 아랫쪽에 있다면.. (-> 감소하는 방향)
            for i in range(y, ny-1, -1): 
                if board[i][x] == '#':
                    return False

    # 모든 조건 검사를 통과했다면, True를 반환
    return True

def trip_search(start, end): # 시작, 끝 좌표 정보를 가지고 해당 여행이 가능한지 평가
    visited = set() # visited는 함수 안에서 한 탐색마다 수행
    q = deque()
    q.append((start[0], start[1], 0, 1)) # (y좌표, x좌표, 걸린 시간, 점프력)을 queue에 주입

    while q: # q가 빌 때까지
        y, x, time, jump_range = q.popleft() # 빼내기
        if y == end[0] and x == end[1]: # 도착지점에 도달했다면
            return time
        
        for i in range(4): # 사방 탐색 (1번 동작 - '점프')
            ny = y + (dy[i] * jump_range) # 점프력에 맞춰서 새로운 좌표를 계산한다
            nx = x + (dx[i] * jump_range) 
            if can_jump(y, x, ny, nx) and (ny, nx, jump_range) not in visited: # 점프가 가능하다면
                visited.add((ny, nx, jump_range))
                q.append((ny, nx, time+1, jump_range)) # 큐에 삽입
        
        if (y, x, jump_range) not in visited: # 2, 3번 동작에 관해서는 같은 좌표에 대해 중복하면 안된다 (-> visited에 없어야만 시도)
            # (y,x)에 대한 모든 액션 q에 삽입된 상태 -> 이젠 방문상태로 바꾼다 (불필요하게 더 이상 queue에 못 들어오게 한다)
            visited.add((y, x, jump_range)) 
            if jump_range >= 1 and jump_range <= 4: # (2번 동작 - '점프력 증가') - 가능한지 평가
                q.append((y, x, time+(jump_range**2), jump_range+1)) # 큐에 해당 정보들 갱신해 삽입
            
            for i in range(jump_range-1, 0, -1): # (3번 동작 - '점프력 감소') - 1~k-1 범위에 대해 수행
                q.append((y, x, time+1, i)) # 큐에 해당 정보들 갱신해 삽입
    
    return -1 # 여기까지 왔으면, 못 구한거임

answers = []
for _ in range(q): # 여행 정보 입력 받기
    r1, c1, r2, c2 = map(int, input().split()) # 시작점(r1,c1), 끝점(r2,c2) 정보 입력 받기
    res = trip_search((r1-1, c1-1), (r2-1, c2-1)) # 가능한지 판단 (-> (1,1)~(N,N) 이므로.. -1씩 해서 들어가야 함)
    print("res 계산 끝남")
    answers.append(res) # 결과에 차례대로 주입

for answer in answers: # 답 출력
    print(answer)
