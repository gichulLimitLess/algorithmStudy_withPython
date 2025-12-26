# 단어 뒤집기 2
'''
    --> 단순히 알파벳들을 뒤집는 테크닉을 쓰는 것보다.. stack을 활용하면 어떨까?
'''
input_val = input()
stack = [] # 스택 자료구조 활용 예정
res = [] # 결과를 저장할 곳

now = 0
# --> stack에는 전부 하나씩만 넣었다 뺐다만 한다: O(2*10만)
while now < len(input_val):
    if input_val[now] == ' ': # 공백일 경우
        while len(stack) > 0: # 스택을 비울 때까지
            res.append(stack.pop()) # 스택 비워서, 하나씩 res에 넣는다 (--> 결과적으로 단어를 뒤집는 꼴임)
        res.append(' ')
    elif input_val[now] == '<': # 태그 오픈인 경우
        while len(stack) > 0: # 스택을 비울 때까지
            res.append(stack.pop()) # 스택 비워서, 하나씩 res에 넣는다 (--> 결과적으로 단어를 뒤집는 꼴임)
        while input_val[now] != '>': # 태그 닫힐 때까지
            res.append(input_val[now])
            now += 1
        res.append(input_val[now]) # 태그 닫히는 거까지 닫는다
    else: # 일반 알파벳, 숫자가 들어오는 경우
        stack.append(input_val[now]) # 스택에 넣는다
    now += 1 # 현재 가리키는 위치에서 +1

# 스택에 남아있는 거 혹시 있다면 처분
while len(stack) > 0:
    res.append(stack.pop())

print(''.join(res)) # 결과 출력