# 문자열 게임 2
'''
    [사고과정]
    문자열 게임 수 T (1 <= T <= 100)
    각 게임마다, 문자열 W (1 <= len(w) <= 10000), 정수 k (1 <= k <= len(w))
    --> 즉, O(100만) 정도로 계산되는데, 선형 시간에 끝낼 수 있는 알고리즘이 필요함
'''
# t = int(input()) # 문자열 게임의 수 t (1 <= t <= 100)
# for _ in range(t):
#     w = input() # 문자열 w
#     k = int(input()) # 정수 k
#     if k == 1: # k가 1이면, 아래 과정을 수행할 필요가 없음
#         print(1, 1)
#     else:
#         answerOfThree = -1 # '3번' 게임에서의 답
#         answerOfFour = -1 # '4번' 게임에서의 답
#         # 1. '3번' 게임 시작 --> O(10000 + 10000)
#         start, end = 0, 0
#         cnt = {}
#         for idx in range(len(w)):
#             if w[idx] not in cnt:
#                 cnt[w[idx]] = 1
#             elif cnt[w[idx]] == k-1: # 지금 셈으로서 해당 알파벳 개수가 k개가 되는 시점이 될 때
#                 end = idx # 끄트머리 저장
#                 while w[start] == w[idx]: # start가 idx가 같아질 때까지
#                     start += 1
#                 break
#             else: # 위 2가지 경우가 모두 아니라면
#                 cnt[w[idx]] += 1 # 증가만 시킨다
#         if start == 0 and end == 0: # 없으면, -1 출력하고, 바로 다음 테케로 넘어간다
#             print(-1)
#             continue
#         else:
#             print(end-start+1, end=' ') # '3번' 게임 정답 출력
#
#         # 2. '4번' 게임 시작 --> O(10000 + 10000)
#         start, end = 0, len(w)-1
#         cnt = {}
#         for idx in range(len(w)): # 우선, 알파벳 개수 세기
#             if w[idx] not in cnt:
#                 cnt[w[idx]] = 1
#             else:
#                 cnt[w[idx]] += 1
#
#         isReverse = False
#         while start < end:
#             # 현재, start 혹은 end에서 존재하고 있는 알파벳의 개수가 정확히 k개인 경우
#             if cnt[w[start]] == k or cnt[w[end]] == k:
#                 if w[start] == w[end]: # 문자열의 첫번째 글자와 마지막 글자가 해당 문자로 같은 최초의 상황이 나왔으면
#                     break # 그것이 정답, 바로 빠져나간다
#                 else:
#                     isReverse = not isReverse  # 방향 뒤집기
#
#             # 진행 방향에 따라 움직인다
#             if not isReverse:
#                 start += 1
#             else:
#                 end -= 1
#
#         print(end-start+1) # '4번' 게임 정답 출력

from collections import defaultdict

T = int(input())
for _ in range(T):
    w = input()
    k = int(input())

    len_w = len(w)
    min_len = 10001
    max_len = 0

    char_cnt = defaultdict(list)
    for i, c in enumerate(w): # 각 문자가 발생한 인덱스를 저장 --> O(10000)
        char_cnt[c].append(i)

    for c, char_index in char_cnt.items(): # O(10000)
        if len(char_index) < k: # 해당 문자의 인덱스 개수(== 문자 개수)가 k개 이하이면
            continue
        for i in range(len(char_index)-k+1): # 문자 인덱스에 대해 슬라이딩 윈도우 진행
            min_len = min(min_len, char_index[i+k-1] - char_index[i]+1) # 최소 길이 연속 문자열
            max_len = max(max_len, char_index[i+k-1] - char_index[i]+1) # 최대 길이 연속 문자열

    if min_len != 10001 and max_len != 0: # 최대/최소가 갱신된 상태라면
        print(min_len, max_len) # 3, 4번 문제 모두, 부분 문자열의 양 끝이 '같은 문자'라는 특징을 이용함
    else:
        print(-1)