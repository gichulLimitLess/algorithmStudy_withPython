# 구간 합 구하기
# --> "접두사 합(prefix sum)"을 이용하면,
# N개의 데이터와 M개의 쿼리에 대해 O(N+M) 시간에 다 구간 합 구해내기 쌉가능

# 데이터의 개수 N과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산 (아래 예제는, 세 번째 수부터 네 번째 수까지..)
left = 3
right = 4
print(prefix_sum[right]-prefix_sum[left-1]) # -> 결과: 70