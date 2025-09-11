# 특정 원소가 속한 집합을 찾기 (parent는 각 노드 번호를 인덱스 삼아 부모를 나타내는 리스트!)
def find_parent(parent, x):
	# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
	if parent[x] != x:
		return find_parent(parent, parent[x])
	return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b: # 더 작은 원소를 더 큰 원소의 부모로 한다
		parent[b] = a
	else:
		parent[a] = b

# 노드의 갯수와 간선(union 연산)의 갯수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
	parent[i] = i

# union 연산을 각각 수행
for i in range(e):
	a, b = map(int, input().split())
	union_parent(parent, a, b)

# 각 원소가 속한 집합 출력 (-> 각 노드가 속해 있는 집합의 최종적인 루트 노드가 출력될 것임!)
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
	print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
	print(parent[i], end=' ')

# ======== 추가 사항 =========
# 위처럼 구할 경우, find 함수가 비효율적으로 동작한다.
# 최악의 경우, find 함수가 모든 노드를 다 확인하는 터라 시간 복잡도가 O(V)가 되버린다는 점이 참 아쉽다..
# 노드의 갯수가 V개, find 혹은 union 연산의 개수가 M개일 때, 전체 시간 복잡도는 O(VM)이 되어 비효율적이다.....