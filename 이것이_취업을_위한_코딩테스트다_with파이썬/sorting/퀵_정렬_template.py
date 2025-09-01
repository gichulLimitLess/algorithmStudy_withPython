# 퀵 정렬
# 리스트에서 첫 번째 데이터를 pivot으로 정하는 형태 (-> 호어 분할 방법)
# 퀵 정렬은 '삽입 정렬'과 다르게 '데이터가 정렬되어 있는 경우'에는 매우 느리게 동작
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
	if start >= end: # 원소가 1개인 경우 종료
		return
	pivot = start # 피벗은 첫 번째 원소
	left = start + 1
	right = end
	while left <= right:
		# 피벗보다 큰 데이터를 찾을 때까지 반복
		while left <= end and array[left] >= array[pivot]:
			left += 1
		# 피벗보다 작은 데이터를 찾을 때까지 반복
		while right > start and array[right] >= array[pivot]:
			right -= 1
		
		if left > right: # left와 right가 엇갈렸다면 작은 데이터와 피벗을 교체
			array[right], array[pivot] = array[pivot], array[right]
		else: # left와 right가 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
			array[left], array[right] = array[right], array[left]
		
		# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
		quick_sort(array, start, right-1)
		quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1) # Quick Sort 스타트
print(array)