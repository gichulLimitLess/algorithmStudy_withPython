# 전깃줄-2
'''
    [사고과정]
    기존의 '전깃줄' 문제는.. A쪽에 연결되어 있는 쪽 기준으로 '오름차순' 정렬
    -> 그 다음에 B쪽에 연결되어 있는 것 기준으로.. LIS 구하는 문제였음
    -> 그런데.. 지금은.. 전깃줄의 개수가 10만 이하의 자연수, 위치의 번호는 50만 이하의 자연수
    -> O(N^2)이 걸리는 기존 dp 방식의 LIS 구하기로는.. 시간 초과 난다!
    ==> 그럼 어떻게 해결해야 하는가? 그럴 때 등장하는 것이.. "이진 탐색"이라고 볼 수 있다
    ==> "LIS의 실제 경로"를 구해야 하는데.. 실제 경로를 구하려면.. parent, pos, 역추적 테크닉을 써야 한다..
        --> 이분 탐색으로 lis 배열 찾는 것은.. 궁극적으로 실제 lis가 아니라.. lis의 길이를 유지하기 위한 임시 후보 배열이다!
'''
# import sys
# from bisect import bisect_left, bisect_right # 이진 탐색할 때 유용히 사용하는 모듈 bisect
#
# input = sys.stdin.readline
#
# lis = []
# partA = []
# n = int(input()) # 전깃줄 개수 n
# lines = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     lines.append((a, b))
#
# lines.sort() # 전깃줄을 A전봇대에 연결되어 있는 기준으로 '오름차순' 정렬 --> O(10만*log10만)
# ans = []
# for a, b in lines: # lines 하나씩 보면서 lis에 넣어보며 탐색
#     loc = bisect_right(lis, b) # 'B전깃줄 관련' 원소가 lis에서 들어갈 위치의 다음 위치를 찾는다 --> O(log10만)
#     if loc < len(lis): # 들어갈 자리가, 현재 lis의 길이 맨 뒤가 아니라면..
#         ans.append(partA[loc]) # 없애야 하는 전깃줄에, 기존 자리에 있던 거의 'A전깃줄' 정보 추가
#         # 교체
#         lis[loc] = b
#         partA[loc] = a
#     else: # 맨 뒤를 가리킨다면
#         # 뒤에 집어 넣는다
#         lis.append(b)
#         partA.append(a)
#
# ans.sort() # 'A전봇대'에 연결되는 위치 번호 오름차순 출력을 위해 정렬
# # 결과 출력
# print(len(ans))
# for e in ans:
#     print(e)

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# 1. A 기준 정렬
lines.sort()

A = [a for a, _ in lines]
B = [b for _, b in lines]

# LIS를 위한 배열들
d = []                  # LIS 배열 (값만)
pos = [0] * n           # i번째 원소가 LIS에서 몇 번째 위치로 들어갔는지
parent = [-1] * n       # LIS 연결 경로

for i in range(n):
    b = B[i]
    # LIS 위치 찾기
    idx = bisect_left(d, b)

    if idx == len(d):
        d.append(b)
    else:
        d[idx] = b

    pos[i] = idx

    # parent 설정
    if idx > 0:
        # pos가 idx-1인 애 중 가장 마지막 i 이전 원소 찾기
        # 뒤에서부터 탐색 (pos[i]==idx인 i는 증가)
        for j in range(i - 1, -1, -1):
            if pos[j] == idx - 1 and B[j] < b:
                parent[i] = j
                break

# 실제 LIS 끝 인덱스 찾기
lis_len = len(d)
last = -1
for i in range(n - 1, -1, -1):
    if pos[i] == lis_len - 1:
        last = i
        break

# LIS 경로 역추적
lis_index = set()
cur = last
while cur != -1:
    lis_index.add(cur)
    cur = parent[cur]

# LIS에 포함되지 않은 A들을 정답으로 출력
ans = []
for i in range(n):
    if i not in lis_index:
        ans.append(A[i])

print(len(ans))
for x in ans:
    print(x)
