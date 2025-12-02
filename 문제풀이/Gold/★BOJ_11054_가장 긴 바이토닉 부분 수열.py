# 가장 긴 바이토닉 부분 수열
'''
    [사고과정]
    가장 긴 증가하는 부분 수열, 가장 긴 감소하는 부분 수열 등과 매우 유사한 문제로 판단
    ---> 그러면 dp를 사용해서 문제 풀어야 할 것 같은데, 어떤 것을 기준으로 dp배열 세울 것인가?

    생각해보면.. 기준 축으로 잡아야 할 것 같은 "냄새"를 Sk로 잡을 수 있을 것 같다
    그리고, Sk를 모든 수열의 원소별로 잡아두고, 그거 기준으로 왼쪽은 증가/오른족은 감소
    --> 어? Sk 기준으로 왼쪽은 Sk보다 작은 원소들 대상으로 "가장 긴 증가하는 부분 수열"
                     오른쪽은 Sk보다 작은 원소들 대상으로 "가장 긴 감소하는 부분 수열"

    레츠고
'''

# n = int(input())
# a = list(map(int, input().split()))
#
# # dp[i] --> i를 Sk(최대값)으로 하는 수열 중에서, 가장 긴 바이토닉 부분 수열의 길이
# dp = [1 for _ in range(n)]
#
# # '가장 긴 증가하는 부분 수열' 길이 계산 후 return
# def LIS(c):
#     # dp_lis[i] --> i번째 원소를 마지막 원소로 하는 것 중 가장 긴 증가하는 부분 수열 길이
#     dp_lis = [1 for _ in range(len(c))]
#     for i in range(len(c)):
#         for j in range(i):
#             if c[i] > c[j]: # '증가하는 부분 수열' 만족하면
#                 dp_lis[i] = max(dp_lis[j] + 1, dp_lis[i])
#     return max(dp_lis)
#
# # '가장 긴 감소하는 부분 수열' 길이 계산 후 return
# def LDS(c):
#     # dp_lds[i] --> i번째 원소를 마지막 원소로 하는 것 중 가장 긴 감소하는 부분 수열 길이
#     dp_lds = [1 for _ in range(n)]
#     for i in range(len(c)):
#         for j in range(i):
#             if c[i] < c[j]: # '감소하는 부분 수열' 만족하면
#                 dp_lds[i] = max(dp_lds[j] + 1, dp_lds[i])
#     return max(dp_lds)
#
# # dp 배열 채워 나가기
# for i in range(n):
#     total = 0
#     # Sk(최댓값) 기준 왼쪽 --> '증가'만 해야 함
#     candidate_left = []
#     candidate_right = []
#     for j in range(i): # --> O(n/2)
#         if a[j] < a[i]: # 기준축(i)의 숫자가 j번째 원소보다 커야만 바이토닉 부분 수열 만족
#             candidate_left.append(a[j])
#     if len(candidate_left) > 0:
#         total += LIS(candidate_left)
#
#     # Sk(최댓값) 기준 오른쪽 --> '감소'만 해야 함
#     for j in range(i+1, n):  # --> O(n/2)
#         if a[j] < a[i]:  # 기준축(i)의 숫자가 j번째 원소보다 커야만 바이토닉 부분 수열 만족
#             candidate_right.append(a[j])
#     if len(candidate_right) > 0:
#         total += LDS(candidate_right)
#     # 이 total + 1이 해당 기준축 기준으로 가장 긴 바이토닉 부분 수열의 길이다!
#     dp[i] += total
#
# # dp로 모아둔 곳에서, 최대값을 뽑아내면...
# # 그게 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력하게 되는 것!
# print(max(dp))

# =============== 위처럼 풀어도 맞긴 했는데, 아래처럼 푸는게 좀 더 빠르고 정석적인 풀이임 ================
# 가장 긴 바이토닉 부분 수열 - 정석 DP 풀이

n = int(input().strip())
a = list(map(int, input().split()))

# 1) lis[i]: i를 마지막으로 하는 증가 부분 수열의 길이
lis = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            lis[i] = max(lis[i], lis[j] + 1)

# 2) lds[i]: i를 처음으로 하는 감소 부분 수열의 길이
lds = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            lds[i] = max(lds[i], lds[j] + 1)

# 3) 각 i를 정점으로 하는 바이토닉 수열의 최대 길이 계산
answer = 0
for i in range(n):
    answer = max(answer, lis[i] + lds[i] - 1)

print(answer)
