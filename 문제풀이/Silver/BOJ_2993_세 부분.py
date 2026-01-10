# 세 부분
from itertools import combinations

input_val = input()
in_len = len(input_val)

selections = [i for i in range(1, in_len)]
res_list = []

# 0~(in_len-1) 까지의 인덱스를 고르는 것 ==> 최악의 경우 49C3
for a, b in combinations(selections, 2):
    # 3개의 부분으로 나누기
    part_1 = input_val[:a]
    part_2 = input_val[a:b]
    part_3 = input_val[b:]

    # 뒤집어서 붙이기
    res_list.append(part_1[::-1] + part_2[::-1] + part_3[::-1])

# 정렬하기
res_list.sort()

# 만들 수 있는 단어들 중, 사전 순으로 가장 앞서는 단어 출력
print(res_list[0])