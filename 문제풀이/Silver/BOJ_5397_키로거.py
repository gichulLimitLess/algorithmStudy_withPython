# 키로거
'''
    중간에 요소를 삽입할 경우, O(N) --> 지금과 같은 문제 제약 조건에선 반드시 시간이 터진다
    --> 중간에 요소를 삽입해도 O(1)으로 만드는 테크닉? --> 연결 리스트
        그리고 그것을 흉내내기 위해.. 스택 2개를 사용해 보는 것!
'''
tc = int(input())
for _ in range(tc):
    cmd_line = input()
    # 스택을 2개로 나누어, 연결 리스트를 흉내내 보려 한다
    # --> left, right 사이에 '커서'가 있다고 생각
    left_stack = []
    right_stack = []
    for cmd in cmd_line: # --> O(100만)
        if cmd == '<': # '왼쪽 화살표'라면
            if len(left_stack) > 0:
                right_stack.append(left_stack.pop())
        elif cmd == '>': # '오른쪽 화살표'라면
            if len(right_stack) > 0:
                left_stack.append(right_stack.pop())
        elif cmd == '-': # '백스페이스'라면
            if len(left_stack) > 0:
                left_stack.pop()
        else: # 그냥 입력 데이터인 경우
            left_stack.append(cmd)

    # 결과적으로 나오는 비밀번호 출력
    for e in left_stack:
        print(e, end='')
    for i in range(len(right_stack)-1, -1, -1):
        print(right_stack[i], end='')
    print()