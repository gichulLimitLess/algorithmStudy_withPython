# 가장 긴 증가하는 부분 수열 2
'''
    [사고과정]
    이전에 풀었던 '전깃줄2' 문제에서의 패턴을 복습해 보자
    --> 이분탐색을 이용해서 LIS를 구하는 것은.. LIS의 길이 자체만을 구하는 것
    ---> 근데 이번 문제에서는, n이 최대 100만이라는 조건 속에서, '길이'만 구하면 됨
         그때 구했던 방식을 상기시키며 LIS의 길이를 구하면 될 듯 하다 (2차원 배열로 푸는 dp로는 불가능)
'''
from bisect import bisect_right, bisect_left

n = int(input())
n_list = list(map(int, input().split()))
lis = [] # 해당 배열 자체는, 이분 탐색으로 구하게 될 경우.. 'lis의 길이를 구하는 임시 배열'임 / 각 원소가 lis는 아님!

for e in n_list: # 하나씩 돌아가면서 진행 --> O(100만 * log100만)
    loc = bisect_left(lis, e)
    if loc >= len(lis): # e가 들어갈 자리가, lis를 넘어간다면
        lis.append(e)
    else: # e가 들어갈 자리가, lis 안에 있다면.. 그것을 교체
        lis[loc] = e

print(len(lis)) # lis 배열의 길이가.. 최종적인 lis 배열의 '길이'를 나타내긴 함