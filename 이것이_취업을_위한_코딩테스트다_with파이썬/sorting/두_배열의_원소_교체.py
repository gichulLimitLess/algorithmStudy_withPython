# 실전 문제 3 - 두 배열의 원소 교체 (180페이지)
# 우선 배열 A는 작은 순서대로(오름차순), 배열 B는 큰 순서대로(내림차순).. 정렬
# B의 첫번째 원소부터 K개의 원소에 대해, A의 첫번째 원소부터 갈아끼면 된다 (B의 해당 원소보다 A의 원소가 작은지도 확인 필수)

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort() # A는 오름차순으로
B.sort(reverse=True) # B는 내림차순으로

for i in range(K): # K개의 원소에 대해서 하나씩 갈아껴야 한다
  if B[i] <= A[i]: # 갈아낄 값이 기존 A의 해당 위치의 값보다 작거나 같아버리면, 더 이상 탐색하는 의미가 없다
    break
  
  # if문에 걸리지 않는 애들은 swap 연산으로 바꿔버린다
  B[i], A[i] = A[i], B[i]

print(sum(A)) # A의 모든 원소의 합 출력 -> 이건 결국 최댓값 출력이 될 것임