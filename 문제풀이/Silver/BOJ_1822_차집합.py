# 차집합
'''
    몇 개의 자연수로 이루어진 두 집합 A, B
    A에는 속하면서 B에는 속하지 않는 모든 원소?
    --> 이거 그냥 set() 쓰면 되는 거 아님?
'''
nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
res = []

for e in A: # A에는 속하면서 B에 속하는지 확인 --> O(50만)
    if e not in B:
        res.append(e)

res.sort() # 구체적인 원소를 빈칸을 사이에 두고 '오름차순'으로 출력하기 위해 정렬 --> O(50만*log50만)
print(len(res)) # A-B 결과 출력
if len(res) != 0: # len(res)가 0이 아닌 경우, 구체적인 원소를 빈칸 사이를 두고 출력
    for e in res:
        print(e, end=' ')