# 회사에 있는 사람
n = int(input())
now_people = set() # 현재 회사에 있는 사람들
for _ in range(n):
    name, order = input().split()
    if order == 'enter': # '출근'인 경우
        now_people.add(name)
    elif order == 'leave': # '퇴근'인 경우
        now_people.discard(name)

n_people_list = list(now_people) # 남아있는 사람들 역순으로 정렬하기 위해 list로 변환
n_people_list.sort(reverse=True)
# 역순으로 한 줄에 한 명씩 출력
for p in n_people_list:
    print(p)