# 실패율
# 이 코드는 프로그래머스에서 돌아가는 거라, 거기서 돌려야 정상 동작함!

def solution(N, stages):
    result = []
    total = len(stages)
    count = {}
    for i in range(1, N+2):
        count[i] = 0
    for stage in stages: # count dict 초기화
        count[stage] += 1
    
    for stage in range(1, N+1): # stages 돌아가며 시작
        if count[stage] == 0: # 도달한 사람이 없다면 실패율 0
            result.append((0, stage))
            continue
        
        now = count[stage]
        fail = now / total
        result.append((fail, stage))
        total -= now # 현재 스테이지까지 도달한 모든 사람 수 갱신
    
    result.sort(key=lambda x: (-x[0], x[1]))
    answer = []
    for e in result: # 스테이지 번호를 answer에 순서대로 저장
        answer.append(e[1])
    return answer

# ============ 오답노트 ==============
# -> 빈도 계산을 하기 위해서는.. 위와 같이 count 딕셔너리 만들어서 빈도수 세는 게 일반적이라고 함!