# 중복 빼고 정렬하기
n = int(input())
input_val = list(map(int, input().split()))
n_list = list(set(input_val))
n_list.sort()
print(*n_list)