# 삽입 정렬
# 데이터가 "거의 정렬"되어 있을 때 매우 유용한 알고리즘이라 할 수 있음
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array_len = len(array)

for i in range(1, array_len):
	for j in range(i, 0, -1): # i번째 원소부터 두번째까지 역으로 거슬러 올라가며 확인
		if array[j] < array[j-1]: # 배열의 앞에 있는 친구가 배열의 뒤에 있는 친구보다 값이 크다면
			array[j-1], array[j] = array[j], array[j-1] # 스왑!
		else: # 아니라면, 해당 과정은 중지해야 함
			break

print(array) # 오름차순 정렬된 결과가 나올 것임