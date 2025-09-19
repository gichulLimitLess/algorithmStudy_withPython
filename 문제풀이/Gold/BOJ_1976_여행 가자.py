# 여행 가자
# --> 간단한 서로소 집합 문제다 / 복습하는 차원에서 한 번 풀어보자

def find_parent(parent, x): # 자기 부모 찾는 것
  if parent[x] != x: # 자기 자신이 아니라면
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union(parent, x, y): # 특정 원소가 속한 집합을 합치는 것
  a = find_parent(parent, x)
  b = find_parent(parent, y)
  if a < b: # 일반적으로 작은 것을 큰 것의 부모로 올린
    parent[b] = a
  else:
    parent[a] = b

n = int(input()) # 도시의 수
m = int(input()) # 여행 계획에 속한 도시들의 수

parent = [i for i in range(n+1)] # 부모는 초기엔 각자 자기 자신으로 해놓는다

for i in range(1, n+1):
  row = list(map(int, input().split()))
  for j in range(len(row)): # 연결된 정보를 토대로 "서로소 집합" 만들기
    if row[j] == 1: # 연결되어 있다 하면
      union(parent, i, j+1) # 1부터 시작하는 점 반영..

# 여행 계획 입력받기
plan = list(map(int, input().split()))

def isPossible(plan):
  prev = parent[plan[0]]
  # 같은 집합 안에 있는지만 확인하면 된다
  for element in plan:
    if parent[element] == prev: # 이전 꺼랑 부모가 같으면
      continue
    else:
      return 'NO' # 중간에 하나라도 걸리면, 못 가는 거다
  return 'YES' # 다 뚫었으면, 갈 수 있는거다

print(isPossible(plan)) # 결과 출력