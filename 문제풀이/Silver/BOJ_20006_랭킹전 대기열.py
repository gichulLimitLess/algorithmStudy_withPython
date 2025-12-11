# 랭킹전 대기열
'''
    [사고과정]
    차분하게 문제에서 주어진 조건대로 구현하면 될 것 같은 문제
'''
# 플레이어 수 p, 방의 정원 m
p, m = map(int, input().split())
rooms = []
# 입력 받는 족족 방에 입장시키기 or 새로운 방 만들기
for _ in range(p):
    level, name = input().split()
    isEnter = False # 방에 입장했는지 여부
    for room in rooms:
        # 처음 입장한 사람 기준으로 레벨이 +-10 차이가 나고, 방이 꽉 차있지 않은 경우
        if abs(room[0][0] - int(level)) <= 10 and len(room) < m:
            room.append((int(level), name)) # (레벨, 닉네임) 주입
            isEnter = True
            break
    if not isEnter: # 여기 나왔는데, 방에 들어간 상태가 아니라면
        rooms.append([(int(level), name)]) # 새로운 방 만들기

# 각 room에 대해서 닉네임 사전순으로 오름차순 정렬 --> 매번 정렬해도 약 O(300log300)임
for room in rooms:
    room.sort(key=lambda x: x[1])

# 출력
for room in rooms:
    if len(room) == m: # 방이 꽉 찼다면 --> 시작시켜야 함
        print("Started!")
    else:
        print("Waiting!")
    # 방에 있는 플레이어들 출력
    for level, name in room:
        print(level, name)
