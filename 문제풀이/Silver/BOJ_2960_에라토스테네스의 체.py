# 에라토스테네스의 체
'''
    에라토스테네스의 체
    -> 그거를 한 번 떠올려 본다
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
deleted = [False] * (n + 1)
cnt = 0

for p in range(2, n + 1):
    if not deleted[p]:               # 아직 안 지워진 가장 작은 p를 찾은 것
        for x in range(p, n + 1, p): # p, 2p, 3p, ...
            if not deleted[x]:
                deleted[x] = True
                cnt += 1
                if cnt == k:
                    print(x)
                    sys.exit()
