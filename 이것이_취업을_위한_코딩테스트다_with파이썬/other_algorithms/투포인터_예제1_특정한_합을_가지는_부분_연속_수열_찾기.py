# 특정한 합을 가지는 부분 연속 수열 찾기
n = 5 # 데이터의 갯수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    # interval_sum이 m보다 크거나 같아졌거나, end가 n에 다다른 경우 나옴
    if interval_sum == m:
        count += 1
    interval_sum -= data[start] # start 포인터가 가리키는 값 빼준다

print(count) # 결과: 3