# 듣보잡
import sys
input = sys.stdin.readline

listen = set() # 듣도 못한 사람
ans = []

n, m = map(int, input().split())
for _ in range(n):
    listen.add(input().strip())

# 보도 못한 사람 쭉 입력 받으면서, listen에 있다면 "듣도 보도 못한 사람"임
for _ in range(m):
    a = input().strip()
    if a in listen: # listen에 있다면
        ans.append(a)

# 사전 순 정렬
ans.sort()
print(len(ans))
for e in ans:
    print(e)