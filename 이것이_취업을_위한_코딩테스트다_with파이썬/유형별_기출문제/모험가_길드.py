# 모험가 길드
# --> 여행을 떠날 수 있는 그룹 수의 최댓값?
n = int(input())
num_list = list(map(int, input().split()))

# 작은 수부터 봐야 최대한 많은 그룹을 만들 수 있다 --> 오름차순 정렬하자
num_list.sort() # 오름차순 정렬

group_cnt = 0
cnt = 0 # 그룹을 만들기 위해서 기준이 되는 친구

for element in num_list: 
  cnt += 1
  if cnt >= element: # 그룹을 하나 결성할 수 있는 경우
    group_cnt += 1
    cnt = 0

print(group_cnt)