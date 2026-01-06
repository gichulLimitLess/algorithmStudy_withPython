# Olympiad Pizza
import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))

q = deque()
for i in range(N):
    # (남은 조각, index)
    q.append((arr[i], i))

ans = [0]*N
time = 0

while q:
    cnt, idx = q.popleft()
    time += 1
    cnt -= 1
    if cnt == 0:
        ans[idx] = time
    else:
        q.append((cnt, idx))

print(*ans)