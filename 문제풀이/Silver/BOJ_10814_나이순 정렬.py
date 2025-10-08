# 나이순 정렬
# --> 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로
order = 0 # 가입한 순서 추적을 위한 변수
n = int(input())
account_list = []
for _ in range(n):
    age, name = input().split()
    # 나이 오름차순, 나이가 같다면 먼저 가입한 사람 오름차순으로 정렬해야 하므로, 이처럼 저장
    account_list.append((int(age), order, name))
    order += 1

account_list.sort() # 오름차순 정렬
for account in account_list:
    print(account[0], account[2]) # 나이, 이름을 공백으로 구분해 출력