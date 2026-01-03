# 카드
'''
    숫자 카드 N장
    --> 가장 많이 가지고 있는 정수 / 여러 개면 작은 거 출력
'''
n = int(input())
n_list = dict()
for _ in range(n):
    a = int(input())
    if a not in n_list: # 없으면
        n_list[a] = 1
    else: # 있으면
        n_list[a] += 1

n_list_res = []
for key, val in n_list.items():
    n_list_res.append((key, val)) # 여기에서 key는 가지고 있는 정수, val은 그 정수의 등장 횟수
n_list_res.sort(key=lambda x: (-x[1], x[0]))
print(n_list_res[0][0]) # 가장 많이 가지고 있는 정수, 그 중에서도 작은 거 출력