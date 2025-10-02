# 공유기 설치
# 집의 개수(N)와 공유기의 개수(C)를 입력받기
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력받기
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진탐색 수행을 위해 정렬 수행

start = 1 # 가능한 최소 거리(min_gap)
end = array[-1] - array[0] # 가능한 최대 거리(max_gap)
result = 0

while start <= end: # 이진탐색 수행
    mid = (start+end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    value = array[0]
    count = 1
    # 현재의 mid 값을 이용해서 공유기를 설치
    for i in range(1, n): # 앞에서부터 차근차근 설치
        if array[i] >= value + mid: # array[i] 값이 array의 맨 첫번째 값과의 차이가 mid보다 작거나 같은 경우
            value = array[i]
            count += 1

    if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1

print(result)

'''
    [오답노트]
    -> 이진 탐색을 이용하는.. '파라메트릭 서치' 유형에 익숙해져야 할 듯! (제대로 된 접근조차 못함)
'''