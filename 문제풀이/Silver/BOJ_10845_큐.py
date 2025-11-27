# 큐
'''
    - 큐를 구현하는 간단한 문제
'''
from collections import deque

q = deque()
n = int(input()) # 명령 개수
for _ in range(n): # --> O(10000)
    a = list(input().split()) # 입력 받고 시작
    if a[0] == 'push': # push X ==> 정수 x를 큐에 넣는 연산
        q.append(int(a[1]))
    elif a[0] == 'pop': # pop ==> 큐에서 가장 앞에 있는 정수 빼고, 그 수 출력 / 없으면 -1
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        if len(q) > 0: # 비어있지 않으면
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)

