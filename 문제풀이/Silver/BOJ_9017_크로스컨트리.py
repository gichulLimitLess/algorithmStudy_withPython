# 크로스 컨트리
'''
    복잡한 알고리즘을 요구하는 것이 아닌, 선수가 몇 명인지 세서 6명 이하인 팀은 제외
    --> 4명까지 더했을 때, 동점이면 5번째를 비교해야 하므로, 5번째는 따로 관리하는게 좋을듯
'''
tc = int(input()) # 테스트 케이스 갯수
for _ in range(tc):
    n = int(input())
    t_list = list(map(int, input().split()))
    score = 1
    team_score = dict() # 팀 누적 점수(상위 4명 주자의 점수만 저장)
    team_cnt = dict() # 팀 멤버 누적 수
    fifth = dict() # 각 팀의 '5번째' 주자의 idx(그냥 언제 들어왔는지 표시)

    # t_list 순회하며 우선 팀 멤버 수 세기 --> O(1000)
    for idx, t in enumerate(t_list):
        if t not in team_cnt:
            team_cnt[t] = 1
        else:
            if team_cnt[t] == 4: # 4명이 동점일 수도 있으니, 미리 기록
                fifth[t] = idx
            team_cnt[t] += 1

    # team_cnt 값이 6 이하인 팀은, 팀의 자격 X, 누적 자체가 안됨 / 다시 순회 --> O(1000)
    score = 1
    for t in t_list:
        if team_cnt[t] >= 6:
            if t not in team_score:
                team_score[t] = [score]
            else:
                if len(team_score[t]) < 4: # 상위 4명만 해야 한다
                    team_score[t].append(score)
            score += 1

    # 누적 점수 별로 오름차순 정렬 --> O(1000+1000log1000)
    score_list = []
    for t_num, s in team_score.items():
        score_list.append((t_num, sum(s), fifth[t_num])) # (팀 번호, 4번째 선수까지의 점수 총합, 5번째 선수가 언제 들어왔는지..)
    score_list.sort(key=lambda x: [x[1], x[2]]) # 점수 기준으로 오름차순 정렬, 4번째 선수까지 동점이면 5번째 선수 기준 오름차순

    # 점수 list 보면서 탐지 -> O(1000)
    for t_num, s, fifth_mem in score_list:
        if team_cnt[t_num] >= 6: # 각 팀의 참가 선수가 여섯보다 작으면 그 팀은 점수 계산에서 제외
            print(t_num) # 점수 기준으로 오름차순 정렬 했으므로, 이 조건을 만족시키는 첫 번째 t_num이 우승팀이다
            break