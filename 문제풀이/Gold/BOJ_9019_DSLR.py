# DSLR
'''
    [사고과정]
    레지스터에 저장되어 있는 n(0 <= n <= 10000)에 대해, 4가지 명령어가 존재
    D: n을 2배로 바꾼다 / 결과가 9999 이상이면, 1만으로 나눈 나머지 취한다 / 그 결괏값을 레지스터에 저장
    S: n에서 1 뺀 결과를 저장 / n이 0일 경우엔 9999가 대신 레지스터에 저장됨
    L: n의 각 자릿수를 왼편으로 회전시켜 그 결과를 저장 / 이 연산하면, 레지스터에 저장된 4자리수는 왼편부터 d2,d3,d4,d1이 된다
    R: n의 각 자릿수를 오른편으로 회전시켜 그 결과를 저장 / 이 연산하면, 레지스터에 저장된 4자리수는 왼편부터 d4,d1,d2,d3이 된다

    Q. 주어진 서로 다른 두 정수 A와 B(A!=B)에 대해 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램?
    --> 각 상황에 대해서, 4가닥으로 뻗어나가는 모든 상황을 고려해야 할 것 같다 / 이건 BFS!
    --> 특정 숫자가 되는 경우에 대해서, 최초로 도달한 시기에 visited 처리해야 한다 (visited가 찍힌 이후에 도착한 것은 절대 최소가 아니기 때문)
    ---> visited로 인해서 모든 숫자는 1번씩만 방문: O(10000*4)? / 계산은 각 횟수마다 1번씩 무조건은 하고.. 'S' 연산 때문에.. 최악의 경우 모든 경우 1번씩 방문은 하니까..
'''
# from collections import deque
# tc = int(input())
#
# # 정확히 '4자리' 수를 만들기 위함
# def make_4digit(a):
#     a_str = str(a)
#     while len(a_str) < 4:
#         a_str = '0' + a_str[:]
#     return a_str
#
# # 'DSLR' 연산을 수행하는 함수
# def DSLR(start, target):
#     q = deque()
#     visited = [False for _ in range(10000)] # 0부터 9999까지의 십진수 저장 가능 --> 그것에 대해서 visited 선언
#     q.append((start, '')) # (시작, 그동안 사용한 명령어) 저장
#     visited[int(start)] = True # 시작지점 방문처리
#     while q:
#         now, inst = q.popleft()
#         if now == target: # target에 도달했다면
#             return inst # 명령어 반환
#         for e in ['D','S','L','R']:
#             if e == 'D': # 1. 명령어가 'D'인 경우
#                 new = (2*int(now))%10000
#                 if not visited[new]: # 방문하지 않았을 경우에만
#                     visited[new] = True
#                     q.append((make_4digit(new), inst+'D'))
#             elif e == 'S': # 2. 명령어가 'S'인 경우
#                 new = (int(now)-1) if int(now) > 0 else 9999
#                 if not visited[new]: # 방문하지 않았을 경우에만
#                     visited[new] = True
#                     q.append((make_4digit(new), inst+'S'))
#             elif e == 'L': # 3. 명령어가 'L'인 경우
#                 new = now[1:]+now[0]
#                 if not visited[int(new)]:
#                     visited[int(new)] = True
#                     q.append((new, inst+'L'))
#             elif e == 'R': # 4. 명령어가 'R'인 경우
#                 new = now[3]+now[:3]
#                 if not visited[int(new)]:
#                     visited[int(new)] = True
#                     q.append((new, inst+'R'))
#
# for _ in range(tc):
#     a, b = input().split()
#     # '4자리 수'를 맞춰야 계산하기 편함 --> 아래처럼 맞춰준다 (자릿수 없는만큼 앞에 0 채워준다)
#     while len(a) < 4:
#         a = '0'+ a[:]
#     while len(b) < 4:
#         b = '0'+ b[:]
#     answer = DSLR(a, b) # DSLR 연산 수행
#     print(answer)

# ==================== 위처럼 문제 풀어도 '맞았습니다' 판정 받을 수 있지만.. 위와 같이 하면 메모리 낭비 좀 있을 수 있음 ====================
# 아래는, 정석적인 '백트래킹' 방법으로 푸는 방법임
from collections import deque
import sys

input = sys.stdin.readline

def op_D(n):
    return (n * 2) % 10000

def op_S(n):
    return 9999 if n == 0 else n - 1

def op_L(n):
    # ex) 1234 → 2341
    return (n % 1000) * 10 + n // 1000

def op_R(n):
    # ex) 1234 → 4123
    return (n % 10) * 1000 + n // 10

def bfs(a, b):
    visited = [False] * 10000
    parent = [-1] * 10000  # parent[x] = 이전 상태
    op_used = [''] * 10000  # op_used[x] = 이 상태로 올 때 사용한 명령어

    q = deque([a])
    visited[a] = True

    while q:
        x = q.popleft()

        if x == b:
            break  # 목적지 도착 → BFS 종료 (최단 경로 확정)

        # 4개 연산을 튜플로 관리
        for nxt, op in [
            (op_D(x), 'D'),
            (op_S(x), 'S'),
            (op_L(x), 'L'),
            (op_R(x), 'R')
        ]:
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt] = x
                op_used[nxt] = op
                q.append(nxt)

    # ----------- 경로 역추적 -----------
    result = []
    cur = b
    while cur != a:
        result.append(op_used[cur])
        cur = parent[cur]

    result.reverse() # 경로 뒤집기
    return ''.join(result)


# ----------- 메인 실행부 -----------
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(bfs(a, b))
