# 문자열 압축
# 이 코드는 프로그래머스에서 돌아가는 거라, 거기서 돌려야 정상 동작함!

def solution(s):
    shortest_val = len(s) # 가장 짧은 길이 우선 "s의 길이"로 해놓기
    
    for step in range(1, len(s) // 2 + 1): # 1부터 s의 길이//2 만큼까지 반복해서 "완전탐색" 해야 함
        compressed = '' # 문자열 추출
        prev = s[0:step] # 비교할 이전 꺼 세팅
        cnt = 1 # 겹치는 부분 문자열 갯수 셀 것임
        
        for i in range(step, len(s), step): # 처음부터 끝까지 s를 step의 길이씩 잘라서 탐색
            if s[i:i+step] == prev: # 이전 꺼와 겹치면
                cnt += 1 # 같은 거 있다고 갯수 올려주기
            else: # 다르면, 이것에 대해서 처리해 줘야 함
                compressed += str(cnt) + prev if cnt >= 2 else prev # cnt가 2보다 클때만 숫자 붙인다
                prev = s[i:i+step]
                cnt = 1
        
        compressed += str(cnt) + prev if cnt >= 2 else prev # cnt가 2보다 클때만 숫자 붙인다
        shortest_val = min(shortest_val, len(compressed)) # 가장 짧은 길이 갱신
    
    return shortest_val
        
# ======== 오답노트 =========
# -> 문자열 처리하는 간단한 방법에 대해서, 그리고 파이썬만의 문법에 대해서 조금 더 익숙해지자!
# -> 진짜 모든 케이스에서 터지지 않도록 하는 것이 제일 중요한 게 "구현/시뮬레이션" 문제이다. 당황하지 말고 차분히!