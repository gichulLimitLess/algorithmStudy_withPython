# 절댓값 힙
'''
    '힙'에다가 절댓값 집어넣고, 그것에 대해서 자료구조 똑바로 사용할 수 있는지 확인하는 문제
    1 <= (연산 개수) <= 10만
    --> (수의 절댓값, 실제 수) 순으로 min heap에 넣으면 될 듯
'''
import heapq

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x != 0: # x가 0이 아닌 경우 --> 배열에 x라는 값을 넣는(추가하는) 연산
        heapq.heappush(q, (abs(x), x))
    else:
        if len(q) > 0: # 배열이 비어 있지 않을 때만 수행
            abs_x, x = heapq.heappop(q)
            print(x)
        else: # 배열이 비어 있다면
            print(0)