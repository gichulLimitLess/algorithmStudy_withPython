# 외벽 점검
# 이 코드는 프로그래머스에서 돌아가는 거라, 거기서 돌려야 정상 동작함!

from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # answer는 절대 len(dist)보다 커질 수 없다, 그래서 일단 이거로 초기화
    
    # weak에서 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 것을 순열로 구해낸다
        for friends in permutations(dist, len(dist)):
            count = 1 # 친구의 수
            position = weak[start] + friends[count-1] # 해당 친구가 점검할 수 있는 마지막 위치
            for index in range(start, start+length): # weak 하나씩 돌면서 모두 방문했는지 확인할 것임
                if position < weak[index]: # 다 못돌아 봤다면
                    count += 1
                    if count > len(dist): # 이미 가용할 수 있는 친구 수를 넘어가 버렸다면
                        break
                    position = weak[index] + friends[count-1]
            
            answer = min(answer, count) # 최솟값 계산
            
    if answer > len(dist):
        return -1
    return answer

# -------- 오답 노트 ----------
# 시뮬레이션, 완전탐색 문제 좀 풀어보니까.. 슬슬 감이 잡히는 게..
# 완탐은.. 내가 문제 조건을 최대한 단순화 하는 게 중요한 것 같고
# 시뮬레이션은.. 문제 조건을 차근차근 따라가는 게 중요한 것 같다!!!