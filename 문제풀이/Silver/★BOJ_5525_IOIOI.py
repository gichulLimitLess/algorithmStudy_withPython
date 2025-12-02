# IOIOI
'''
    [사고과정]
    - 슬라이딩 윈도우 할 지.. 아니면 그냥 자료구조 써서 '연속된 짝을 이루는 개수' 구할지...
        --> 하다가, deque 써서 그냥 '연속된 짝을 이루는 개수' 구하기로 함
'''
# from collections import deque
#
# n = int(input())
# m = int(input())
# s = list(input())
# q = deque()
#
# ans = 0
# # s를 하나씩 본다 --> 모든 원소가 q에 한번씩 들어갔다 나왔다 할 수 있으므로.. 최대 O(200만)
# for e in s:
#     if e == 'O': # 'O'일 경우
#         if len(q) > 0 and q[-1] == 'I': # q의 맨 마지막 원소가 'I'일 경우 --> 짝을 이룰 수 있음
#             q.append(e)
#         else: # 아니면, 짝을 못이룸 --> 현재까지 누적된 것에서 Pn이 몇개 나올수 있는지 계산하고, 큐 비우기
#             if (len(q) // 2) >= n:
#                 ans += ((len(q) // 2) - n + 1)
#             while q: # 큐 비우기
#                 q.popleft()
#     elif e == 'I': # 'I'일 경우
#         if len(q) > 0 and q[-1] == 'O': # q의 맨 마지막 원소가 'I'일 경우 --> 짝을 이룰 수 있음
#             q.append(e)
#         else: # 아니면, 짝을 못이룸 --> 현재까지 누적된 것에서 Pn이 몇개 나올수 있는지 계산하고, 큐 비우기
#             if (len(q) // 2) >= n:
#                 ans += ((len(q) // 2) - n + 1)
#             while q:
#                 q.popleft()
#             q.append(e) # 'I'로 시작해야 하므로, 이거는 집어 넣는다
#
# # 맨 마지막 경우에 대해서 flush 해줘야 한다
# if s[-1] == 'I':
#     if (len(q) // 2) >= n:
#         ans += ((len(q) // 2) - n + 1)
#     while q:
#         q.popleft()
#
# print(ans)

n = int(input())
m = int(input())
s = input().strip()

i = 0
cnt = 0      # 연속된 "IOI" 개수
ans = 0

while i < m - 2:
    if s[i:i+3] == "IOI":
        cnt += 1
        if cnt >= n:
            ans += 1
        i += 2  # "IOI"에서 뒤의 "I"로 점프 (겹치기 허용)
    else:
        cnt = 0
        i += 1

print(ans)
