# 수 정렬하기 5
n = int(input())
n_arr = []
for _ in range(n):
    n_arr.append(int(input()))

# 이 자체가 비내림차순으로 정렬됨
n_arr.sort()
for e in n_arr:
    print(e)
