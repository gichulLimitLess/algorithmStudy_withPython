# 옥상 정원 꾸미기
'''
    O(N^2)으로 문제를 풀 경우.. 8만*8만 -> O(64억)
        => 절대 시간 안에 해결 불가능
    --> 그러면 그 방법 말고 다른 방법을 사용해야 함
        => O(N), O(NlogN) 안에 풀 수 있는 방법?
    --> "스택"을 사용하면 될 것 같다.
'''
# n = int(input()) # 빌딩 개수
# h_list = []  # 각 빌딩 높이 hi
# for _ in range(n):
#     h_list.append(int(input()))
# stack = [] # 스택에는 (건물 번호, 높이)가 원소로 들어갈 것임
# info_dict = dict() # key: 건물 번호(0~n-1) / value: 볼 수 있는 건물 개수
# for i in range(n):
#     info_dict[i] = 0
#
# # --> O(8만 * 2) / 충분히 시간 안에 해결 가능!
# for idx, h in enumerate(h_list):
#     # 지금 들어올려는 것이, 스택 맨 위에 있는 것보다 작다면
#     if len(stack) == 0 or stack[-1][1] > h:
#         stack.append((idx, h))
#     else: # 지금 들어올려는 것이, 스택 맨 위에 있는 것보다 크다면
#         cnt = 0
#         while len(stack) > 0 and stack[-1][1] <= h:
#             info_dict[stack[-1][0]] += cnt
#             stack.pop() # 스택에서 맨 위 요소 제거
#             cnt += 1
#         if len(stack) > 0: # 여기는 따로 계산해줘야 함
#             info_dict[stack[-1][0]] += cnt
#         stack.append((idx, h))
#
# # 스택에 남아있는 거 처리
# cnt = 0
# while len(stack) > 0:
#     info_dict[stack[-1][0]] += cnt
#     stack.pop()
#     cnt += 1
#
# res = 0
# for e in info_dict.values():
#     res += e
# print(res) # 결과 출력

'''
    우리는 보통 "미래의 상황을 확정할 수 없다" (우리는 항상 과거만 알고, 미래는 모른다)
    --> 그렇기에 '지금 확정 가능한 것'만 세야 한다
    --> 그런 과정에서, "관점을 뒤집을 필요"도 있을 수 있다.
    (위 문제에 대해서는, 지금 빌딩에서 볼 수 있는 건물 개수를 세지 말고..
        "특정 빌딩을 볼 수 있는 왼쪽(과거)의 건물 개수"를 세자
        그렇게 하면, 스택에는 '현재 빌딩을 볼 수 있는 빌딩'만을 남기게 된다
'''
