# 최대 힙
'''
    1. 배열에 자연수 x 넣기
    2. 배열에서 가장 큰 값 출력하고, 그 값을 배열에서 제거
    ---> Python은 최소 힙만을 제공하므로, 부호 바꿔서 넣고, 뺄 때 부호 바꿔서 출력하도록 해야 함
'''
import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input()) # 입력된 숫자
    if x == 0: # x가 0이라면 -> 배열에서 가장 큰 값 출력하고 그 값을 배열에서 제거하기
        if len(q) > 0:
            print(-heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, -x) # '최대 힙'은 - 붙여서 넣어야 한다