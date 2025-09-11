# 실전 문제 1 - 팀 결성
# (1 <= N, M <= 100,000)
# 팀 합치기 연산: 0 a b / 같은 팀 여부 확인 연산: 1 a b / a와 b는 N 이하의 양의 정수
# 같은 팀 여부 확인 연산에 대해 한 줄에 하나씩 YES 또는 NO로 결과 출력
# --> 이거.. 빼박 union-find 문제임, 복습하는 느낌으로 레츠고 (-> N,M의 최대치가 둘 다 10만이므로.. 경로 압축해서 시간 복잡도 개선 필요)

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, x, y):
  a = find_parent(parent, x)
  b = find_parent(parent, y)

  if a < b: # 더 큰 친구가 자식 노드가 되도록 설정
    parent[b] = a
  else:
    parent[a] = b

N, M = map(int, input().split()) # N, M 입력받기
parent = []
for i in range(N+1): # parent 배열 초기에는.. 부모를 자기 자신으로 초기화
  parent.append(i)

for _ in range(M): # M번 연산 수행
  calc_type, a, b = map(int, input().split())
  if calc_type == 0: # '팀 합치기' 연산 수행해야 한다면 
    union_parent(parent, a, b)
  elif calc_type == 1: # '같은 팀 여부 확인' 연산 수행해야 한다면
    if find_parent(parent, a) == find_parent(parent, b): # 같은 집합이라면
      print("YES")
    else: # 아니라면
      print("NO")