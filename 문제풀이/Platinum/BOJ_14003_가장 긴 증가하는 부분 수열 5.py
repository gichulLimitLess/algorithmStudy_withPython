# 가장 긴 증가하는 부분 수열 5
'''
    [사고과정]
    이 문제 또한 '전깃줄2' 문제와 거의 궤를 같이 하는 문제
    --> 그 때 당시의 패턴을 빠르게 되새겨 보는 차원에서 풀어보려 하는 문제
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