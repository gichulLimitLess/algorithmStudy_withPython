# 정렬되어 있는 두 리스트의 합집합
# --> 병합 정렬에서 사용되는 알고리즘
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 리스트 A와 B의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
result = [0] * (n+m)
i = 0 # a 배열에 대해서 가리키는 pointer
j = 0 # b 배열에 대해서 가리키는 pointer
k = 0 # result 배열에 대해서 가리키는 pointer

# 하나씩 result 리스트를 채워 나가본다
while i < n or j < m:
    if j >= m or (i < n and a[i] <= b[j]): # a 배열이 가리키고 있는 거를 넣어야 하는 경우
        result[k] = a[i]
        i += 1 # a 배열에 대해 가리키고 있는 포인터 += 1
    else: # b 배열이 가리키고 있는 거를 넣어야 하는 경우
        result[k] = b[j]
        j += 1 # b 배열에 대해 가리키고 있는 포인터 += 1
    k += 1 # result 배열에 대해 가리키고 있는 포인터 += 1

# 결과 출력
for i in result:
    print(i, end=' ') # 결과: 1 2 3 4 5 6 8