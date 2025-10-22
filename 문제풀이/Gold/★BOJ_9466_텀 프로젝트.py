# 텀 프로젝트
'''
    --> 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램 작성
    2 <= n <= 10만, 학생들은 1부터 n번까지 번호 부여

    Q. 같은 팀인지 어떻게 구별하면 될까?
        -> 테스트 케이스를 직접 손으로 써본 결과, 특정 index에 적혀 있는 수를 index 삼아서
            지속적으로 탐색했을 때..
            => 특정 지점으로 돌아온다 -> 사이클 발생 -> 팀 하나 완성
            => 중간에 끊긴다 -> 사이클 발생 x -> 같은 팀에 속할 수 x
    n은 최대 10만이기 때문에, 재귀로 단순히 로직을 구성하면 메모리가 터질수도 있을 듯 / 반복문으로 구현하자
    스택을 사용하면 효율적일 것 같다는 생각이 들었다
'''
tc = int(input()) # 테스트 케이스 개수
for _ in range(tc): # 테스트 케이스 갯수만큼 반복
    n = int(input()) # 학생 수
    info_list = [0] # 선택된 학생들의 번호
    info_list += list(map(int, input().split()))
    team_member_cnt = 0
    state = [0] * (n+1) # 0: 미방문, 1: 방문 중(스택 경로), 2: 사이클 완료
    for i in range(1, n+1): # 1부터 n까지 탐색
        if state[i] == 0: # 방문하거나, 방문 중인 state가 아니라면
            stack = []
            # 사이클 찾을 때까지 찾아 들어간다
            now = i
            while True:
                if state[now] == 0:
                    stack.append(now)
                    state[now] = 1
                    now = info_list[now]
                elif state[now] == 1:  # 사이클 발견
                    while True:
                        member = stack.pop()
                        state[member] = 2
                        team_member_cnt += 1 # 사이클에 들어가 있는 학생 수를 센다
                        if member == now: # 자기 자신을 다시 발견 했다면
                            break
                    while stack: # 나머지들에 대해서도 처리 (-> 얘네는 사이클에 들어가 있는 학생 수로 치면 X)
                        state[stack.pop()] = 2
                    break
                else:  # state[now] == 2 → 이미 처리된 경로 / 탐색할 필요 X
                    while stack:
                        state[stack.pop()] = 2
                    break

    print(n - team_member_cnt) # n에서 사이클 들어간 학생수만큼 빼면, 그냥 그게 "팀에 포함되지 못한 사람 수"임