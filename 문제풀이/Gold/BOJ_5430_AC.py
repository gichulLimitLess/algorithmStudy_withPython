# AC
'''
    [사고과정]
    - 해당 문제에서 가장 조심해야 할 것은.. 'R' 연산
        --> 'R' 연산 나올 때마다 reverse 해버리면.. 매번 O(10만) / 이걸 10만번 하게 되면 시간 터짐
    ==> 다른 방법을 떠올려야 하는데.. 그 중 효율적으로 사용할 만한 것은 '투 포인터'
'''
t = int(input())
ans = []
for _ in range(t):
    isError = False # '에러 발생' 플래그
    p = input() # 수행할 함수 p
    n = int(input()) # 배열에 들어있는 수의 개수 n (0 <= n <= 10만)
    in_input = input().lstrip('[').rstrip(']') # --> 문자열 파싱 수행: O(10만)
    num_list = list(map(int, in_input.split(','))) if in_input != '' else []

    # 투 포인터 설정
    start = 0
    end = len(num_list)-1
    dir = 1 # 방향 설정 ('R' 명령어 만날 때마다 뒤집어 준다 / 1: 정방향, -1: 역방향)
    for e in p: # 명령 하나씩 수행 --> O(10만)
        if e == 'R': # '뒤집기' 수행해야 한다면
            dir = -dir # 부호 바꿔준다 (== 방향 바꿔준다)
        elif e == 'D': # '첫 번째 수 버리기' 수행해야 한다면
            if dir == 1:  # 정방향이라면
                start += 1
            else:  # 역방향이라면
                end -= 1

            # 위 과정을 수행하고 나서, 오류가 났다면 == 배열 비어있는데 수행했다는 것..
            if start > end and start-end > 1: # 배열 비어있다는 것 == 옆의 조건
                isError = True
                break

    # 결과 저장
    if not isError:
        if dir == -1: # 역방향이면, 역방향 출력시켜야 함
            res = []
            for i in range(end, start-1, -1):
                res.append(str(num_list[i]))
            if len(res) > 0:
                ans.append('[' + ','.join(res) + ']')
            else:
                ans.append('[' + ']')
        else: # 정방향 출력
            res = []
            for i in range(start, end+1):
                res.append(str(num_list[i]))
            if len(res) > 0:
                ans.append('[' + ','.join(res) + ']')
            else: # 비어있으면.. 이렇게 해야 함
                ans.append('[' + ']')
    else:
        ans.append('error')

# 결과 출력
for answer in ans:
    print(answer)