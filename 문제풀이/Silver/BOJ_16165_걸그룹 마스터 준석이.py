# 걸그룹 마스터 준석이
'''
    퀴즈의 종류:
        0 -> 팀의 이름을 주고, 팀에 속한 멤버 이름을 사전순으로 한 줄에 하나씩 출력
        1 -> 멤버의 이름을 주고, 해당 멤버가 속한 팀의 이름을 출력
'''
# 총 입력 받을 걸그룹 수 n, 맞춰야 할 문제 수 m
n, m = map(int, input().split())
teamToMember = dict()
memberToTeam = dict()
for _ in range(n): # 걸그룹 수만큼 반복
    teamName = input()
    memberNum = int(input())
    members = []
    for _ in range(memberNum):
        members.append(input())
    members.sort() # 해당 팀에 속한 멤버 이름 사전순 출력을 위해 정렬
    teamToMember[teamName] = members
    for member in members:
        memberToTeam[member] = teamName

for _ in range(m): # 퀴즈 시작
    order = input()
    cmd = input()
    if cmd == '0': # 0 -> 팀의 이름을 주고, 팀에 속한 멤버 이름을 사전순으로 한 줄에 하나씩 출력
        for member in teamToMember[order]:
            print(member)
    elif cmd == '1': # 1 -> 멤버의 이름을 주고, 해당 멤버가 속한 팀의 이름을 출력
        print(memberToTeam[order])