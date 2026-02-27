# 수 정렬하기 4
n = int(input())
n_arr = []
for _ in range(n):
    n_arr.append(int(input()))

# 내림차순 정렬 후 출력하기
n_arr.sort(reverse=True)
for e in n_arr:
    print(e)