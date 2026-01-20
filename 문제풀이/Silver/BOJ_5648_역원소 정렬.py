# 역원소 정렬
n_list = []
res = []
count = 1000000001
while len(n_list) < count:
    n_input = input().split()
    if count == 1000000001: # count가 안 채워져 있다면
        count = int(n_input[0])
        for e in n_input[1:]:
            n_list.append(e)
    else:
        for e in n_input:
            n_list.append(e)

# 뒤집기 --> O(100만 * 12)
for e in n_list:
    res.append(int(e[::-1]))

# 정렬 --> O(100만 * log100만)
res.sort()

# 출력
for e in res:
    print(e)