# 창고 다각형
'''
    [사고과정]
    특별한 알고리즘을 요하는 것은 아님
    --> 예외사항 잘 체크하고 푸는 방법 세우면 되는 문제
'''
# n = int(input()) # 기둥의 개수 n
# infos = []
# for _ in range(n):
#     l, h = map(int, input().split())
#     infos.append((l, h)) # (왼쪽 면의 위치, 높이)
#
# infos.sort() # "왼쪽 면의 위치" 기준 오름차순 정렬
#
# # infos 하나씩 살펴보면서 진행
# cp = 0 # 체크포인트
# i = 1
# total = 0 # 총 넓이 저장
# while i < n: # 끝까지 갈 때까지 확인
#     if infos[i][1] > infos[cp][1]: # 가다가 부닥친다먄
#         total += (infos[i][0] - infos[cp][0]) * infos[cp][1] # (가로*세로) 해서 저장
#         cp = i # 체크포인트 갱신
#     i += 1
#
# # 이렇게 해서 끝까지 갔어, 이제 마지막에 후속 처리 해주어야 함
# total += infos[cp][1] # 넓이 1짜리 하나 처리하고 시작해야 함
# while cp < n-1: # 체크 포인트 끝까지 갈 때까지
#     nxt_idx = 0
#     max_val = 0
#     for i in range(cp+1, n): # 남아있는 부분에서 최대값 찾아야 함
#         if infos[i][1] > max_val:
#             max_val = infos[i][1]
#             nxt_idx = i
#
#     total += (infos[nxt_idx][0]-infos[cp][0]) * infos[nxt_idx][1] # 최소 넓이를 위해 이렇게 곱해서 누적
#     cp = nxt_idx # 다음으로 바로 점프
#
# print(total) # 결과 출력

# ============= 위처럼 풀어도 맞긴 하는데, 아래 풀이가 좀 더 깔끔하고 정석 풀이임 =============
n = int(input())

lst = []
result = 0
for i in range(n) :
    a,b = map(int,input().split())
    lst.append([a,b])
#기둥을 x축 순으로 정렬한다.
lst.sort()

#가장 높은 기둥의 번호를 알아낸다.
i = 0
for l in lst :
    if l[1] >result :
        result = l[1]
        idx = i
    i += 1

#초기 높이는 첫번째 기둥의 높이
height = lst[0][1]

#최대 높이전까지 돌면서 다음 기둥이 현재보다 높으면
#result에 현재의 면적을 계산해서 더해주고 높이를 다음 기둥으로 갱신한다.
for i in range(idx) :
    if height < lst[i+1][1] :
        result += height * (lst[i+1][0]-lst[i][0])
        height = lst[i+1][1]
    #아니면 그냥 현재면적을 더해준다.
    else :
        result += height * (lst[i+1][0] - lst[i][0])

#뒤에서부터도 똑같이 진행한다.
height = lst[-1][1]

for i in range(n-1, idx, -1) :
    if height < lst[i-1][1] :
        result += height * (lst[i][0]-lst[i-1][0])
        height = lst[i-1][1]
    else :
        result += height * (lst[i][0] - lst[i-1][0])

print(result)