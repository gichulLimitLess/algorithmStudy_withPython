'''
    이분 탐색으로 lis의 '길이'를 구할 때는..
    lis에.. 각 lis의 '최소 끝값'을 저장하게 되면.. 'lis'의 길이 자체를 구할 수 있음
    그러나, 그게 lis의 '실제 원소'를 뜻하는 것이 아님
    --> 실제 원소를 구하기 위해서는.. 수열 a에 대해서, 각 원소가 lis에서 들어갈 수 있는 위치를 저장하고
        뒤에서부터 쭉 훑으며 복원시키는 게 핵심임!
    (아래 풀이 코드는, 해당 문제의 대표 패턴 문제 격인 '백준 - 가장 긴 증가하는 부분수열 5' 문제의 풀이 코드)
'''

from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
lis = [] # lis 배열은.. 각 길이의 lis 중 가능한 최소 끝값을 저장한 임시 배열
idx_list = [0 for _ in range(n)] # idx_list 배열은.. a의 각 원소가 lis의 몇번째(0~n-1)로 들어갈 수 있는지 저장한 배열

# a를 뒤지면서 레츠고 --> O(100만 * log100만)
for idx, e in enumerate(a):
    loc = bisect_left(lis, e)
    if loc >= len(lis): # loc의 위치가 lis의 길이를 넘어간다면
        lis.append(e)
    else: # loc의 위치가 lis의 한가운데에 있다면 --> '가능한 최소 끝값' 갱신
        lis[loc] = e
    idx_list[idx] = loc # 들어갈 수 있는 위치 idx_list에 집어 넣기

# lis의 길이 우선 구하기
lis_len = len(lis)
real_lis = []

imsi = lis_len - 1
# idx_list 뒤에서부터 살펴보며 진짜 lis 원소 찾기 --> 백트래킹 (O(100만))
for i in range(n-1, -1, -1):
    if idx_list[i] == imsi: # 해당 자리에 들어갈 수 있는 원소 발견 --> 넣고, imsi - 1
        real_lis.append(a[i])
        imsi -= 1

real_lis.reverse() # 뒤집어야 정답이 된다

# 결과 출력
print(lis_len)
for e in real_lis:
    print(e, end=' ')