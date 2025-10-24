# 퇴사
'''
    [오답노트]
    - i일을 선택했을 때 결과가 '미래의 최적 해'에 달려 있음
        -> 즉, 미래를 알아야 현재의 최적 선택을 계산 가능한데..
        -> 미래의 결과를 모르는 상태에서 현재를 계산하려니 점화식이 막혔음
    - DP는.. 앞에서부터 누적해야 할 수도 있고, 뒤에서부터 거꾸로 풀어야 할 수도 있다.
        -> 현재 상태가 미래에 의존하는가, 과거에 의존하는가를 먼저 판단하자.
        -> 앞에서부터 푸는 게 막히면, 반드시 "뒤집어서 정의"해보는 습관을 들여야 한다.
    - "선택지 분기"로 점화식을 세우자
        -> DP의 점화식은 대부분 "선택지 중 최적해" 구조
'''

# 사실, 얘는 n이 최대 15이므로, 완전탐색 해도 상관 없다
n = int(input())
info_list = [tuple(map(int, input().split())) for _ in range(n)]
max_benefit = 0

def dfs(day, total):
    global max_benefit

    # dfs(재귀 호출)에서의 기저 조건
    if day >= n:
        max_benefit = max(max_benefit, total)
        return

    # 1. 상담을 진행하는 경우
    if day + info_list[day][0] <= n:
        dfs(day + info_list[day][0], total + info_list[day][1])

    # 2. 상담을 하지 않고 다음 날로 넘어가는 경우
    dfs(day + 1, total)

dfs(0, 0)
print(max_benefit)