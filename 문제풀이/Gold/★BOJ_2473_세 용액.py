# # 세 용엑
# '''
#     [사고과정]
#     3 <= (용액의 수 N) <= 5000
#     --> 절대 5000 Combination 3으로는 시간 내에 풀이할 수 없다. ==> 약 O(20억)
#     --> 투포인터 + 이분탐색으로 3개의 조합을 찾아내 보는 방식은? ==> 약 O(2 * 5000 * log5000)
# '''
# n = int(input())
# num_list = list(map(int, input().split()))
# num_list.sort() # num_list 정렬 --> O(5000 * log5000)
#
# # 투 포인터를 설정한다 (-> 초기엔 '양 끝으로')
# first = 0
# second = len(num_list)-1
# best_combi = []
# min_val = int(3*1e9) # 최소값을 저장할 min_val
#
# # first, second를 고정한 상태로 진행
# while first+1 < second: # 가운데 숫자 하나가 들어갈 자리가 있어야 한다, 그래서 while문 조건 이렇게!
#     # 나머지 하나의 값을 구해야 한다
#     start = first
#     end = second
#     local_min = int(3*1e9)
#     # 이 'imsi' 변수에, 지금 이분탐색으로 찾으러 가는 3번째 수를 더했을 때, 0에 가장 가까운 거 구하러 간다
#     imsi = num_list[first] + num_list[second]
#     third = -1
#
#     # "이분탐색"으로 찾는다
#     while start <= end:
#         mid = (start + end) // 2
#         if local_min > abs(num_list[mid] + imsi):  # 0에 더 가까운 조합을 찾았으면
#             local_min = abs(num_list[mid] + imsi)  # first, second 고정한 상태에서 local_min 갱신
#             third = mid  # third 갱신
#
#         # 양수라면.. --> mid 기준으로 "왼쪽"을 찾아서 "더 작은 애"를 만들 수 있나 확인해야 함
#         if num_list[mid] + imsi >= 0:
#             end = mid - 1
#         # 음수라면.. --> mid 기준으로 "오른쪽"을 찾아서 "더 큰 애"를 만들 수 있나 확인해야 함
#         elif num_list[mid] + imsi < 0:
#             start = mid + 1
#
#     # 현재, local_min에는 현재 고정된 first, second 조합에서 만들 수 있는 가장 0에 가까운 "절댓값"이 저장되어 있음
#     # 그것이, 전역에 저장되어 있는 min_val보다 작은지 확인하고, 만약 더 작을 경우, 갱신한다.
#     if min_val > local_min:
#         min_val = local_min
#         best_combi = [num_list[first], num_list[third], num_list[second]]
#
#
#     # first, second 투 포인터 이동은..
#     # num_list[first] + num_list[second] + num_list[third] 값이 양수, 음수인지에 따라 조절한다
#
#     # 3개의 조합에 대해서 값을 구했을 때, 그게 양수면.. --> "큰 쪽"을 줄여서 최대한 0에 가깝게 만들어야 한다
#     if num_list[first] + num_list[second] + num_list[third] >= 0:
#         second -= 1
#     # 3개의 조합에 대해서 값을 구했을 때, 그게 음수면.. --> "작은 쪽"을 키워서 최대한 0에 가깝게 만들어야 한다
#     else:
#         first += 1
#
# # best_combi에는 0에 가장 가깝게 만드는 3개의 조합을 '오름차순'으로 저장하고 있을 것이다
# print(best_combi[0], best_combi[1], best_combi[2])

# 세 용액 (정답 풀이)
'''
    [사고 과정]

    N (3 ≤ N ≤ 5000)
    → 3개를 단순 조합하면 O(N^3) → 최대 1.25e11 → 절대 불가능

    "세 수의 합이 0에 가장 가까운 조합"을 찾아야 한다.
    → 핵심 패턴: 1개는 고정하고, 나머지 2개를 투포인터로 탐색 (Two-Pointer: O(N^2))

    전체 알고리즘:
    1) num_list 오름차순 정렬
    2) i번째 수를 고정 (i = 0 ~ N-3)
    3) left = i+1, right = N-1 로 두고 투포인터로 탐색
    4) 합이 0보다 크면 right ↓, 합이 0보다 작으면 left ↑
    5) 절댓값이 최소일 때마다 정답 갱신
'''

import sys
input = sys.stdin.readline

# 1. 입력
n = int(input())
num_list = list(map(int, input().split()))

# 2. 정렬 (투포인터 사용을 위한 필수 조건)
num_list.sort()

min_val = float('inf')    # 현재까지 찾은 "0과의 최소 차이"
best_combi = []           # 정답(3개의 용액 조합) 저장

# 3. 첫 번째 값을 고정하며 전체 탐색
for i in range(n - 2):       # i는 0 ~ n-3
    left = i + 1             # 투포인터 시작점 (i 바로 오른쪽)
    right = n - 1            # 투포인터 끝점 (맨 오른쪽)

    # 4. left < right 범위 내에서 투포인터 진행
    while left < right:
        s = num_list[i] + num_list[left] + num_list[right]  # 3개의 합

        # 0과의 차이가 더 작으면 정답 갱신
        if abs(s) < min_val:
            min_val = abs(s)
            best_combi = [num_list[i], num_list[left], num_list[right]]

        # 합이 0보다 큰 경우 → 값을 줄여야 한다 → right를 왼쪽으로 이동
        if s > 0:
            right -= 1
        # 합이 0보다 작은 경우 → 값을 키워야 한다 → left를 오른쪽으로 이동
        else:
            left += 1

# 5. best_combi는 정렬된 상태이므로 바로 출력 가능
print(best_combi[0], best_combi[1], best_combi[2])
