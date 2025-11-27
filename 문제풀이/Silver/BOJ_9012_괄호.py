# 괄호
'''
    [사고과정]
    스택을 사용해서 풀어야 하는 전형적인 '짝' 맞추기 문제
    --> 주어진 괄호 문자열 하나씩 스택에 넣으면서..
        맨 위꺼랑 짝(짝은 무조건 '(', ')' 순이어야 함) 맞춰지면 같이 빼내고.. 아니면 계속 넣고..해서
        최종적으로 스택에 남아있는게 없으면 VPS / 아니면 VPS 아님
    --> 한 번 수행 당.. O(50)
'''
tc = int(input())
result = []
for _ in range(tc):
    stack = []
    input_str = input() # 입력 받기
    for e in input_str:
        if len(stack) > 0 and stack[-1] == '(' and e == ')': # 짝을 이뤄야만
            stack.pop()
        else: # 짝을 이루지 못한다면, 집어 넣어야 한다
            stack.append(e)

    if len(stack) == 0: # 모두 짝 지어서 나갔다면
        result.append('YES')
    else:
        result.append('NO')

# 결과는 표준 출력 활용 --> 하나씩 출력
for res in result:
    print(res)
