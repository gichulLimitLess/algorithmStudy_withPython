# 특정 원소가 속한 집합을 찾기 (parent는 각 노드 번호를 인덱스 삼아 부모를 나타내는 리스트!)
def find_parent(parent, x):
	# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

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
# 위 코드의 시간 복잡도는.. 노드의 갯수가 V개이고, 최대 V-1개의 union 연산과 M개의 find 연산이 가능하다 할 때.. O(V + M(1+log2-M/V V))라는 것이 알려져 있대요..
# 예를 들어, 노드의 갯수가 1000개, union + find 연산이 약 100만번이라 하면.. 1000만번의 연산이 필요하다고 이해하면 될 듯
# ---> 증명 과정은 책 범위가 아니어서.. 패스하도록 하겠다.