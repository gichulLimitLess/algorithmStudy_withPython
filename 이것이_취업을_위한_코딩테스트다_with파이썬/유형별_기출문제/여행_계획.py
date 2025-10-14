# 여행 계획
# --> 여행 계획에 포함되어 있는 여행지들이 모두 "서로소 집합"에 있는지 확인하면 됨
def find_parent(parent, x):
    if parent[x] != x: # 부모가 자기 자신이 아니면
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b: # 더 작은 놈을 부모로 둘 예정
        parent[b] = a
    else:
        parent[a] = b

def find_answer(parent):
    plan = list(map(int, input().split()))  # 계획에 대해 입력 받기
    prev = find_parent(parent, plan[0])
    for location in plan:  # plan 하나씩 찾아가며, 모두 같은 부모인가 확인(==같은 집합인가 확인)
        if find_parent(parent, location) != prev: # 하나라도 이전꺼랑 부모가 다르다면, 계획은 수행될 수 없음
            return "NO"

    return "YES"

n, m = map(int, input().split()) # 여행지 개수 n, 계획에 포함된 여행지 수 m
adj_matrix = []
parent = [i for i in range(n+1)] # 처음에는 부모가 각자 자기 자신임
for i in range(n): # 하나씩 인접 행렬에 집어 넣기
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:  # 연결되어 있다고 표시되면, 이미 있다면..
            union(parent, i + 1, j + 1)  # 한 집합으로 합친다

print(find_answer(parent)) # 결과 출력