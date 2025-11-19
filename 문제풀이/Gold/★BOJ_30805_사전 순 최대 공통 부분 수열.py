# LCS 2
'''
    [다시 푸는 문제]
    -> "편집 거리"와 비슷하게 푸는 문제였음
    -> 2차원 dp 테이블을 만드는 것으로 패턴 적용해보기
        dp[i][j] -> A의 i번째 문자까지의 부분 문자열,
                    B의 j번째 문자까지의 부분 문자열을 고려했을 때, LCS 길이
    -> 전이식
        A[i] == B[j]라면..
        왼쪽 대각선 방향의 dp[i-1][j-1] 값에 +1 해서 dp[i][j]에 저장
        아니라면...
        dp[i-1][j], dp[i][j-1] 값 중에서 더 큰 값으로 갱신
    -> LCS 구하기
        길이를 구해가는 과정에서 모두 집어넣고, 비교하는 연산을 할 경우, 각 상황에 대한 부분 LCS 필요
        이럴 경우에는.. dp 테이블에 더해, 부분 문자열 테이블까지 상황별로 모두 필요할 수 있음 (--> 메모리 터질 듯)
        LCS 문자열 자체는.. 지금까지 dp 테이블을 채워온 방식을 역이용 하면 된다 / 백트래킹 써보자
        현재 위치의 문자열이 서로 같다면.. 대각선 방향으로 올라가고 해당 위치의 문자열을 넣는다
        다르다면.. 대각선 방향으로 올라가면서, 해당 칸의 문자를 answer_rev에 넣기 --> 0번째 행 or 0번째 열까지 갔으면 백트래킹 종료
'''

# A = input()
# B = input()
# # 아예 빈칸도 포함해야 함
# dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
#
# # dp 테이블 채우기
# for i in range(1, len(A)+1):
#     for j in range(1, len(B)+1):
#         if A[i-1] == B[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1 # 대각선에서 값 땡겨오기 -> 그러고 +1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#
# print(dp[-1][-1]) # LCS의 길이 우선 출력
# if dp[-1][-1] != 0: # 길이가 0이 아니면, LCS 자체를 출력
#     answer_rev = []
#     # 백트래킹 실시
#     sy = len(A)
#     sx = len(B)
#     while sy != 0 and sx != 0: # 첫번째 행 또는 열에 가기 전까지 반복
#         # 대각선 방향에서, 값이 같은 게 아니라.. 지금 현재 위치에서 비교하고 있는 "문자"가 같은지 확인해야 한다
#         if A[sy-1] == B[sx-1]:
#             answer_rev.append(A[sy-1])
#             sy -= 1
#             sx -= 1
#         else: # 이외의 경우, 왼쪽 or 위쪽으로 가봐야 한다 (해당하는 칸의 문자는 포함 시키지 X)
#             if dp[sy - 1][sx] > dp[sy][sx - 1]:  # 위쪽이 왼쪽보다 값이 더 큰 경우
#                 sy -= 1
#             else:
#                 sx -= 1
#
#     answer_rev.reverse() # 뒤집는다
#     print(''.join(answer_rev)) # 결과 출력

'''
    [이번 풀이에서 간과한 것]
    문제에 'LCS' 이야기가 있다고 해서 무조건 LCS 구하듯이 풀면 안된다는 것이다.
    순서 보존의 필요성부터 먼저 확인해야 했고, LCS는 여러 개일 수 있다는 것을 간과했다.
    그리고, 공통된 수 중 '가장 큰 수'부터 뽑아서, 지속적으로 그 다음으로 작은 공통 숫자 찾아가는 것이 핵심..
        --> 각 사건이 독립이고, 매 선택이 최적의 선택임을 입증... 이거 그리디다!
        --> 근데.. 순서 유지를 해야 되잖아? 그러면... 어떻게?
'''
import sys
import bisect
input = sys.stdin.readline

# ----------------------------
# 1. 입력 받기
# ----------------------------
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# ----------------------------
# 2. 값 -> 등장 위치 리스트 만들기
#    subsequence 조건(순서 유지)을 위해
#    각 값이 어디에서 등장하는지 인덱스를 다 기록해둔다.
# ----------------------------
positions_in_A = dict()
positions_in_B = dict()

for idx, value in enumerate(A):
    if value not in positions_in_A:
        positions_in_A[value] = []
    positions_in_A[value].append(idx)

for idx, value in enumerate(B):
    if value not in positions_in_B:
        positions_in_B[value] = []
    positions_in_B[value].append(idx)

# ----------------------------
# 3. 두 수열에 공통으로 등장하는 값 목록 추출
#    그리고 "사전 순 최대" 조건을 위해
#    값들을 내림차순으로 정렬한다.
# ----------------------------
common_values = sorted(
    set(positions_in_A.keys()) & set(positions_in_B.keys()),
    reverse=True
)

# ----------------------------
# 4. subsequence 조건을 위한 포인터 준비
#    - last_idx_A : A 수열에서 우리가 마지막으로 선택했던 위치
#    - last_idx_B : B 수열에서 우리가 마지막으로 선택했던 위치
#    처음에는 어떤 것도 선택하지 않았으므로 둘 다 -1에서 시작
# ----------------------------
last_idx_A = -1
last_idx_B = -1

result = []   # 최종 정답 수열

# ----------------------------
# 5. 큰 값부터 하나씩 선택해 보기
# ----------------------------
for value in common_values:

    # value가 A에서 등장한 모든 인덱스 목록
    posA_list = positions_in_A[value]
    # value가 B에서 등장한 모든 인덱스 목록
    posB_list = positions_in_B[value]

    # "부분 수열" 조건 때문에,
    # 항상 last_idx_A보다 오른쪽에 있는 위치만 선택 가능하다.
    # bisect_left는 "정렬된 리스트에서 어떤 값 이상이 처음 등장하는 위치"를 찾는다.
    iA = bisect.bisect_left(posA_list, last_idx_A + 1)
    iB = bisect.bisect_left(posB_list, last_idx_B + 1)

    # posA_list[iA], posB_list[iB] 둘 다 유효한 위치가 있다면
    # value를 선택할 수 있다.
    while iA < len(posA_list) and iB < len(posB_list):
        # value 선택!
        result.append(value)

        # 선택된 위치로 포인터 갱신
        last_idx_A = posA_list[iA]
        last_idx_B = posB_list[iB]

        # 다음 선택을 위해
        # 다시 last_idx_A 이후에서 value를 찾는다.
        iA = bisect.bisect_left(posA_list, last_idx_A + 1)
        iB = bisect.bisect_left(posB_list, last_idx_B + 1)


# ----------------------------
# 6. 정답 출력
# ----------------------------
print(len(result))
print(*result)