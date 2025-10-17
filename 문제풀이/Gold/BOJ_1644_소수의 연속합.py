# 소수의 연속합
from math import sqrt

n = int(input())
# 1. '에라토스테네스의 체'를 활용해서, 1~n까지의 소수를 모두 구한다
isPrime = [True for i in range(n+1)]
isPrime[0] = False
isPrime[1] = False

for i in range(2, int(sqrt(n))+1): # -> O(4*400만) 걸림
    if isPrime[i] == True:
        j = 2
        while i*j <= n: # n까지, i 자기 자신을 제외하고, 모두 소수가 아님을 표시
            isPrime[i*j] = False
            j += 1

prime_numbers = []
for i in range(len(isPrime)): # -> O(400만) 걸림
    if isPrime[i]: # 소수인 것이 판명될 때만, prime_numbers에 넣기
        prime_numbers.append(i)

if n < 2:
    print(0)
elif n == 2:
    print(1)
else:
    start, end = 0, 0
    res, cnt = 0, 0
    while True: # -> O(400만) 걸림
        if res >= n:
            if res == n:
                cnt += 1
            res -= prime_numbers[start]
            start += 1
        else:
            if end == len(prime_numbers):
                break
            res += prime_numbers[end]
            end += 1

    print(cnt) # 답 출력