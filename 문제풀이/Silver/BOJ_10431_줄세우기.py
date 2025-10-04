# 줄세우기
p = int(input())
result = []
for _ in range(p):
    num_list = list(map(int, input().split()))
    tc_num = num_list[0]
    students = num_list[1:]
    now_standing = [] # 지금 서 있는 친구들
    total_steps = 0 # 총 뒷걸음질 수
    for k, student in enumerate(students): # students 하나씩 보면서 레츠고
        now_standing.append(student) # 한 명씩 맨 뒤에 세운다
        if len(now_standing) > 1: # 2명 이상 서있을 때만 아래 process 진행
            for i in range(len(now_standing) - 1): # 맨 뒤 직전까지 비교 연산 진행
                if now_standing[i] > student: # 키가 가장 큰 학생 중 가장 앞에 있는 애 발견
                    total_steps += (k-i)
                    a = now_standing.pop() # 맨 뒤에 애를 일단 뺀다
                    now_standing.insert(i, student) # 해당하는 구역에 넣는다
                    break # 찾았으니 종료

    print(tc_num, total_steps)