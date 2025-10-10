# 0 만들기
from itertools import product
from collections import deque

tc = int(input())

for _ in range(tc): # 각 tc마다 계산 수행
    n = int(input())
    num_list = [i for i in range(1, n+1)] # 숫자 저장
    signs_list = ['+', '-', ' '] # 기호 저장
    answers = set()

    for combi in product(signs_list, repeat=len(num_list)-1): # 중복 조합으로 기호 정렬
        # 계산을 편리하게 하기 위해, stack 2개 선언
        nums_queue = deque()
        signs_queue = deque()
        res = '' # 수식 저장
        prev = ''
        for j in range(len(num_list)-1): # signs_list 길이 만큼만 반복 진행
            prev += str(num_list[j]) # 우선, 숫자 누적
            res += (str(num_list[j]) + combi[j]) # 수식 저장
            if combi[j] != ' ': # 기호가, 공백이 아니면
                nums_queue.append(int(prev))
                signs_queue.append(combi[j])
                prev = ''
            # 기호가 공백이면, prev += num_list[j] 작업만 누적하면 된다

        # num_list의 마지막 부분 처리
        prev += str(num_list[n-1])
        res += (str(num_list[n-1]))
        nums_queue.append(int(prev))

        # stack 하나씩 끌어올려 보며, 계산
        total_calc = nums_queue.popleft()
        while len(nums_queue) != 0 or len(signs_queue) != 0:
            sign = signs_queue.popleft()
            number = nums_queue.popleft()
            if sign == '+': # 여기에는, 덧셈 뺄셈밖에 없다
                total_calc += number
            else:
                total_calc -= number

        if total_calc == 0: # 결과가 0이라면
            answers.add(res)

    a = sorted(list(answers)) # 아스키코드 기준 오름차순 정렬
    for answer in a: # 결과 출력
        print(answer)
    print() # 각 테스트 케이스의 결과는 한 줄 띄워 구분한다

'''
    [참고사항]
    - 난 너무 과도하게 구현 난이도를 높이는 습관이 있다 (사실 파이썬 내장 함수를 잘 몰라서 그러는 것도 있다)
        -> 이 문제에서는, eval(), replace() 등을 쓰면 훨씬 간편하게 풀 수 있다
'''