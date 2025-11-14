# 사이클 게임
'''
    [사고 과정]
    - 선분 그리기를 했을 때.. 사이클 판별하라고?
        --> 그림 그려보니.. 이건 노드 간의 '연결 관계'를 파악하는 것 / 와우! '서로소 집합'
    - 서로소 집합을 통해서.. 두 노드를 연결하려 할 때, 그 두 노드의 부모가 같을 경우.. 그건 '사이클 발생'
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(500000) # 아무리 path compression 적용한다 하더라도, 최초 1회는 이럴 수 있으므로.. 풀어는 놓겠다

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split()) # 평면 상의 점 n개, instruction m개
first_tp = 0
parent = [i for i in range(n)] # 부모를 나타내는 배열 parent --> 처음엔 '자기 자신'

instruction_list = []
for i in range(m): # input 입력 받기 --> O(100만)
    a = list(map(int, input().split()))
    instruction_list.append(a)

for idx, e in enumerate(instruction_list): # m개의 instruction 수행 --> O(100만)
    a, b = e
    if find_parent(parent, a) == find_parent(parent, b): # 사이클 발생하는 시기 처음으로 발견!
        first_tp = idx+1
        break
    else: # 아니라면, 계속 합쳐간다
        union(parent, a, b)

print(first_tp) # 결과 출력