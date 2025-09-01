# 계수 정렬
# 데이터의 갯수 N, 최댓값 K라 가정
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
# max()를 이용해서 최댓값을 찾아야 하니, O(N)이 걸릴 것임
count = [0] * (max(array) + 1) 
count_len = len(count)
array_len = len(array)

# 여기에서, 각 데이터에 해당하는 값을 count에서 증가시키는 것은 O(N)이 걸릴 것임
for i in range(array_len):
	count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값을 count에서 증가시킨다

for i in range(count_len): # 갯수 정보를 저장한 리스트 count에 기록된 정렬 정보 확인 / 약 O(K) 걸릴 것임
	for j in range(count[i]):
		print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 각 인덱스 출력(count에서 인덱스는 array에서 각 원소 값임)

# 결과적으로 O(2N+K), 약 O(N+K)가 걸린다고 시간 복잡도 계산 가능