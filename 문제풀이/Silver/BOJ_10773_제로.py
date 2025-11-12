# 제로
# --> 간단한 스택 문제

k = int(input())
stack = []
for _ in range(k):
    a = int(input())
    if a == 0: # 정수가 0인 경우, 위에 꺼를 뺀다
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))