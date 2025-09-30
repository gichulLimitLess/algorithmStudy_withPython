# deque 연습하는 문제
from collections import deque

n = int(input())
q = deque()

for _ in range(n): # 명령 갯수대로 반복
  op = list(input().split())
  if op[0] == 'push_front':
    q.appendleft(int(op[1]))
  elif op[0] == 'push_back':
    q.append(int(op[1]))
  elif op[0] == 'pop_front':
    if q:
      print(q.popleft())
    else:
      print(-1)
  elif op[0] == 'pop_back':
    if q:
      print(q.pop())
    else:
      print(-1)
  elif op[0] == 'size':
    print(len(q))
  elif op[0] == 'empty':
    if q: # 비어있지 않다면
      print(0)
    else:
      print(1)
  elif op[0] == 'front':
    if q:
      print(q[0])
    else:
      print(-1)
  elif op[0] == 'back':
    if q:
      print(q[len(q)-1])
    else:
      print(-1)