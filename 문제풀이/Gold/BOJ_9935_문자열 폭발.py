# 문자열 폭발
'''
    [사고과정]
    - 폭발 문자열을 일일이 찾아서, 확인해도 되는지의 여부를 체크
        --> 문자열 길이 최대 O(100만)
        --> 쪼개진 문자열 다시 join하는 데 최대 O(100만)
        --> 위의 프로세스를 최악의 경우.. 최대 O(50만)번 반복할 수도 있음 / 위처럼 진행하면 안됨
    - 그러면.. 스택을 사용하는 것은?
        --> 폭발 문자열 최대 길이가 36,
            스택에 들어올 때마다 스택 맨 위에서부터 36 길이의 문자열 확인하는 거 100만번.. 확인해 봐야 O(3600만)
'''
input_str = input()
bomb_str = input()
stack = [] # 스택을 활용해서 문제 풀이 진행

# '폭발 문자열'인지 검사
def isBombStr(stack, bomb_str):
    idx = len(bomb_str)-1
    for i in range(len(stack)-1, len(stack)-len(bomb_str)-1, -1):
        if stack[i] != bomb_str[idx]:
            return False
        idx -= 1
    # 다 통과했으면, 폭발 문자열인 것이다
    return True

# 입력된 문자열에 대해서 하나씩 stack에 넣어보며 확인 (-> O(100만 * 36))
for e in input_str:
    stack.append(e)
    # stack에 폭발 문자열 길이보다 더 많은 문자열이 들어와 있고
    # stack의 위에서부터 bomb_str의 길이만큼 쭉 훑었을 때, bomb_str와 같은 경우
    if len(stack) >= len(bomb_str) and isBombStr(stack, bomb_str):
        for k in range(len(bomb_str)): # --> O(36)
            stack.pop()

# 결과 출력
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))