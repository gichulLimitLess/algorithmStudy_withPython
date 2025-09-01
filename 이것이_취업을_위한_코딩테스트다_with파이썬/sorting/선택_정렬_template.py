# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array_len = len(array)

for i in range(array_len):
	min_index = i # 가장 작은 원소의 인덱스
	for j in range(i+1, array_len):
		if array[min_index] > array[j]: # 가장 작은 게 추가로 발견된다면?
			min_index = j
		
		array[i], array[min_index] = array[min_index], array[i] # Python에선 Swap 연산 많이 사용!

print(array) # 오름차순 정렬된 결과가 나올 것임