# 시그마
'''
    [사고과정]
    문제가 겁나 길다.
    근데, 문제가 길면, 독해만 한다면 그리 어렵지 않은 문제일 수 있음
    --> 차분히 읽고 문제를 풀어보자
'''
from math import gcd

p = 1000000007
m = int(input()) # 주사위 개수 m (1 <= m <= 10^4)
ans = 0
for _ in range(m): # m개의 줄에 걸쳐 각 주사위의 정보 나타냄
    ni, si = map(int, input().split())
    a, b = si // gcd(ni, si), ni // gcd(ni, si)
    # 파이썬에서는, '페르마의 소정리'를 활용해 이와 같이 모듈러 역원을 쉽게 구할 수 있음
    ans += (a*pow(b, -1, p)) % p
    ans %= p
print(ans)
