# 차이를 최대로
from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))
max_val = 0

for permu in permutations(num_list, n):
    permu_list = list(permu)
    val = 0
    for i in range(n-1):
        val += abs(permu_list[i] - permu_list[i+1])
    max_val = max(max_val, val)

print(max_val)