# '문자열 뒤집기'에서 풀었던 문제임
# --> 0과 1의 그룹(slice) 중.. 더 적은 갯수의 slice를 가진 것을 바꿔야 한다

val_list = list(input())
now = int(val_list[0])
list_len = len(val_list)
group_cnt = [0, 0]

for i in range(1, list_len):
  if now != int(val_list[i]): # 이전 꺼와 같지 않은 경우 --> 그룹 수를 세줘야 함
    group_cnt[now] += 1
    now = int(val_list[i])

group_cnt[now] += 1 # 마지막 그룹에 대해서.. 이거 한 번 해줘야 함

print(min(group_cnt)) # 더 작은 값이 다솜이의 최소 횟수