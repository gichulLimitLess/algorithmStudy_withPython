# 공항
'''
    [풀이]
    - i번째 비행기를 1번부터 gi(1 <= gi <= G)번째 게이트 중 하나에 영구적으로 도킹
        --> 최대한 많은 비행기를 도킹 시키기 위해선?
            주어진 gi에 대해서, 현재 연결된 "서로소 집합" 중에서 가장 오른쪽을 그 "왼쪽"과 연결시켜야 한다
        --> 이것은 직접 그림을 통해서, 그렇게 하면 될 것이란 "냄새"를 맡았다
        --> 틀린 문제를 다시 풀어보는 것으로, 빠르게 "접근"하는 법을 연습함
'''
def find_parent(parent, x):
    if parent[x] != x: # 자기 자신이 아니라면
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if x < y: # 더 작은 애를 부모로 둔다
        parent[y] = x
    else:
        parent[x] = y

g = int(input()) # 게이트 수 g (1 <= g <= 10^5)
p = int(input()) # 비행기 수 p (1 <= p <= 10^5)
parent = [i for i in range(g+1)] # 0부터 g까지 parent 관련한 정보 만들기 (처음엔 자기 자신)
gi_list = []

for _ in range(p): # gi에 대한 정보 p개가 주어짐
    gi = int(input())
    gi_list.append(gi)

plane_cnt = 0
# gi를 하나씩 뒤져 보면서 하나씩 찾아본다
for gi in gi_list:
    # gi가 속해 있는 집합의 부모가 0이라면
    # ---> 해당 범위에 있는 모든 게이트가 점령당한 상태 / 공항 운영 중지해야 함
    if find_parent(parent, gi) == 0:
        break
    else:
        # 아니라면, 지금 현재 gi의 parent와 그 parent 왼쪽에 있는 애를 union 한다
        union(parent, find_parent(parent, gi), find_parent(parent, gi)-1)
        plane_cnt += 1 # 비행기 개수 하나 +1

print(plane_cnt) # 이것이 승원이가 도킹시킬 수 있는 최대 비행기 수