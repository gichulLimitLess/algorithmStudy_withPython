# IF문 좀 대신 써줘
'''
    dict와 이분탐색을 적절히 쓰면 시간 초과 안되지 않을까?
'''
from bisect import bisect_left
import sys
input = sys.stdin.readline
res = []

n, m = map(int, input().split())
# 칭호는 전투력 상한값의 비내림차순으로 주어짐
names = dict() # key: 전투력 상한값 / value: 칭호명
for _ in range(n): # ---> O(10^5)
    name, maxVal = input().split()
    if int(maxVal) not in names: # 어떤 캐릭터의 전투력으로 출력 가능한 칭호가 여러 개면, 가장 먼저 입력된 거 하나만 출력
        names[int(maxVal)] = name

damage_list = list(names.keys()) # 이거 자체가 '비내림차순'으로 되어 있음 --> O(10^5*log10^5)]
for _ in range(m): # ---> O(10^5)
    char_damage = int(input().rstrip())
    res.append(names[damage_list[bisect_left(damage_list, char_damage)]]) # --> O(log10^5)

# 결과 출력
for e in res:
    print(e)