# N번째 큰 수
'''
    [사고과정]
    조금 생각해보면.. N^2 크기의 표에서..
    ---> 모든 수는 자신의 한 칸 위에 있는 수보다 크다
    ---> 그렇지만, 그 줄의 모든 수가 윗줄에 있는 모든 수보다 크다는 건 아니다
    --> 그리고, 메모리 초과를 방지하려면.. 한줄씩 해결해야 할 것 같다
'''
# import copy
#
# n = int(input()) # n
# first = list(map(int, input().split()))
# first.sort(reverse=True)  # O(1500*log1500)
# for _ in range(n-1): # O(1500)
#     nxt = list(map(int, input().split()))
#     nxt.sort(reverse=True)  # O(1500*log1500)
#     new = []
#     f_p = 0
#     n_p = 0
#     while len(new) < n: # O(1500) / merge 느낌으로 풀어볼까?
#         if first[f_p] > nxt[n_p]:
#             new.append(first[f_p])
#             f_p += 1
#         else:
#             new.append(nxt[n_p])
#             n_p += 1
#     # first를 갱신한다
#     first = copy.deepcopy(new) # O(1500)
#     first.sort(reverse=True) # O(1500*log1500)
#
# print(first[n-1]) # 이게 n번째로 큰 수

# ========= 위처럼 풀어도 936ms로 맞긴 함, 하지만 '힙'으로 푸는게 더 나을수도 =========
import heapq

n = int(input())
h = []

for _ in range(n):
    # 한 줄씩 입력받기
    row = list(map(int, input().split()))
    # row 뒤져보면서, heap이 꽉 안차있으면 넣기
    # 꽉 차있으면, 힙의 맨 위에 있는 것(그건 n번째 큰 수)보다, 지금 들어온 게 더 크다면, 그걸로 교체
    for x in row:
        if len(h) < n:
            heapq.heappush(h, x)
        else:
            if h[0] < x:
                heapq.heapreplace(h, x)

print(h[0])
