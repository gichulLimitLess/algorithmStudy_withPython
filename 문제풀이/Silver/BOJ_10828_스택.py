# 스택
'''
--> 스택 자체는 python에서 list로 구현 가능
명령 총 5가지:
  push X: 정수 X를 스택에 넣는 연산이다.
  pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
  size: 스택에 들어있는 정수의 개수를 출력한다.
  empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
  top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input()) # 1 <= N <= 10000 (N은 명령의 갯수)
stack = []

for _ in range(N): # 명령의 갯수만큼 수행
  input_val = list(input().split())
  if input_val[0] == 'push': # 삽입 연산 수행
    stack.append(int(input_val[1])) 
  elif input_val[0] == 'pop': # 빼내기 연산 수행
    if len(stack) == 0: # 만약 스택에 들어있는 정수가 없다면
      print(-1)
    else:
      print(stack.pop())
  elif input_val[0] == 'size': # 스택의 길이를 출력하는 연산 수행
    print(len(stack))
  elif input_val[0] == 'empty': # 스택이 비어있는지 여부 수행
    if len(stack) == 0: # 비어있다면
      print(1)
    else:
      print(0)
  elif input_val[0] == 'top': # 스택 가장 위의 정수 출력
    if len(stack) == 0: # 비어있다면
      print(-1)
    else:
      print(stack[-1])
