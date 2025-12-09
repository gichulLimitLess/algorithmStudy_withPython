# 완전제곱수
from math import sqrt

INF = int(1e9)

m = int(input())
n = int(input())
min_val = INF
total = 0
for i in range(m, n+1):
    if int(sqrt(i))**2 == i: # 완전제곱수일 경우
        min_val = min(min_val, i)
        total += i

if total != 0:
    print(total)
print(min_val if min_val != INF else -1)