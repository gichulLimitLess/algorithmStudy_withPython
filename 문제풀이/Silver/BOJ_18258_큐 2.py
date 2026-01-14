# 큐 2
from collections import deque
import sys

input = sys.stdin.readline

q = deque()

n = int(input().rstrip())
for _ in range(n):
    instr = list(input().split())
    if instr[0] == 'push': # push 연산
        q.append(int(instr[1]))
    elif instr[0] == 'pop': # pop 연산
        if len(q) == 0: # 들어있는 게 없으면
            print(-1)
        else:
            print(q.popleft())
    elif instr[0] == 'size': # size 연산
        print(len(q))
    elif instr[0] == 'empty':
        print(1 if len(q) == 0 else 0)
    elif instr[0] == 'front':
        print(q[0] if len(q) > 0 else -1)
    elif instr[0] == 'back':
        print(q[-1] if len(q) > 0 else -1)