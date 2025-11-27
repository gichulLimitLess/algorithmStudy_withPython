# 카드2
'''
    N의 최대 크기가 50만번
    --> 정직하게 50만번 정해진 액션 수행하면 됨
    (유의: 단순하게 list 쪼개기 문법(list[:1]) 이런 거 써가지고 하면.. O(N) 걸리는 것이니..
         '시간 초과' 나는지 확인할 필요 있음 --> 이 문제의 경우에는 시간 초과 나므로.. deque 사용함)
'''
from collections import deque

n = int(input())
q = deque()
for i in range(1, n+1):
    q.append(i)

while len(q) > 1: # 카드 1장 남을 때까지 반복
    q.popleft() # 제일 위에 있는 카드 바닥에 버리기
    imsi = q.popleft() # 제일 위에 있는 카드도 빼내기
    q.append(imsi) # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다

print(q[0])