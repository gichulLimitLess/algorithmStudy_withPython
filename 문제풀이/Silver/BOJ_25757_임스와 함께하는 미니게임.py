# 임스와 함께하는 미니게임
'''
    우선 set으로 모아 놓고..
    --> 이미 있는 경우, pass
    --> 위의 경우의 수를 구하면 된다
'''
n, game = input().split()
max_p = 0
# 임스를 제외한 게임별 참여 인원
if game == 'Y':
    max_p = 1
elif game == 'F':
    max_p = 2
elif game == 'O':
    max_p = 3
users = set()
cnt = 0
for _ in range(int(n)): # 유저 정보 입력 받기
    users.add(input())

print(len(users) // max_p) # 이게 정답임