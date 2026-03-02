"""
   카드 1
   -> 제일 위에 있는 카드를 바닥에 버리고
   -> 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
   ===> n(1 <= n <= 1000)이 주어졌을 때, 제일 마지막에 남게 되는 카드의 번호 순서대로 출력
"""
from collections import deque

n = int(input())
# 카드 앞에 꺼를 넣었다가 뒤로 넣어야 하는 것은.. deque 써야 할 것 같다
card_list = deque()
for i in range(1, n+1):
    card_list.append(i)

# 문제의 요구사항에 맞게 출력
for _ in range(n):
    print(card_list.popleft(), end=' ')
    if len(card_list) > 0:
        card_list.append(card_list.popleft())