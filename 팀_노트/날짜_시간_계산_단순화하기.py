'''
    1. 시간(HH:MM) 계산 기본형
    --> 문자열 시간 차이를 계산할 때는 반드시 '분 단위'로 변환하라
    [팁]
    - 무조건 split(':')로 파싱
    - 뺄셈 결과가 음수일 가능성이 있으면 abs() 고려
    - 23:59 기준 보정 시 23*60+59 = 1439 활용
'''
def to_minutes(time_str: str):
    # 'HH:MM' 문자열을 분 단위로 변환
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def diff_minutes(t1: str, t2: str):
    # 시간 차이 계산 (단위: 분)
    return to_minutes(t2) - to_minutes(t1)

# 예시
print(diff_minutes("05:34", "07:59")) # 결과: 145(분)

'''
    2. 날짜(YYYY-MM-DD) 계산 기본형
    --> "윤년 제외 / 매달 30일" 문제에서 자주 쓰이는 형태
    [팁]
    - "날짜 차이" 문제에서 datetime 대신 이거 쓰면 안전
    - 시간 제한 1초 내에서 O(1) 계산
    - abs() 써서 순서 무관하게 처리 가능
'''
def to_days(date_str: str):
    # 'YYYY-MM-DD' 문자열을 총 일수로 변환 (윤년 제외, 매달 30일)
    y, m, d = map(int, date_str.split('-'))
    return y*360 + m*30 + d

def diff_days(d1: str, d2: str):
    return abs(to_days(d2) - to_days(d1))

# 예시
print(diff_days("2025-01-01", "2025-01-11")) # 결과: 10(일)

'''
    3. 달별 일수 고려(윤년 제외) 버전
    --> 날짜가 조금 더 현실적으로 주어질 때 (ex. 1월~12월 실제 일수)
    [팁]
    - 윤년을 고려하지 않아도, 실제 문제에서는 대부분 이 정도까지만 요구
    - sum()은 O(12) -> 사실상 O(1)
    - 코테에 "윤년 무시" 명시되어 있으면 아래 코드 그대로 써도 된다
'''
def to_days_real(date_str: str):
    y, m, d = map(int, date_str.split('-'))
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    return y * 365 + sum(month_days[:m-1]) + d

def diff_days_real(d1: str, d2: str):
    return abs(to_days_real(d2) - to_days_real(d1))

# 예시
print(diff_days_real("2025-01-01", "2025-03-01")) # 결과: 59(일)

'''
    4. 시간 + 날짜 복합형 (ex. 주차장, 근무시간, 로그 누적)
    --> 날짜/시간 둘 다 문자열로 주어지는 복합 시뮬레이션 문제에서 유용
    [활용 포인트]
    - 날짜가 넘어가는 시간 곗간에 완벽하게 대응 (ex. "23:59 ~ 00:10")
    - 주차요금, 출퇴근 기록, 장비 작동 시간 등 시뮬레이션 문제에 매우 유용
'''
def to_minutes_full(datetime_str: str) -> int:
    #'YYYY-MM-DD HH:MM'을 절대 분 단위로 변환
    date_part, time_part = datetime_str.split()
    y, m, d = map(int, date_part.split('-'))
    h, min_ = map(int, time_part.split(':'))
    return (y * 360 + m * 30 + d) * 24 * 60 + h * 60 + min_

# 예시
t1 = "2025-10-08 23:59"
t2 = "2025-10-09 00:10"
print(to_minutes_full(t2) - to_minutes_full(t1))  # 결과: 11(분)

'''
    [최종 정리]
    날짜/시간 문제 = 문자열 파싱 + 단위 통일 + 조건 경계 처리
    1. 문자열을 수 단위(분/일)로 변환해라
    2. 경계값(23:59, 00:00)은 항상 엣지케이스로 확인해라
    3. "윤년 무시/매달 30일"은 계산 단순화의 신호다 -> 수식화로 접근해라
'''