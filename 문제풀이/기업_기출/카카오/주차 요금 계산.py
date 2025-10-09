# 주차 요금 계산
# 이 코드는 프로그래머스에서 돌아가는 거라, 거기서 돌려야 정상 동작함!

import math

def calc_time(in_time, out_time):  # 시간을 계산해주는 함수
    time = 0
    if int(in_time[3:]) > int(out_time[3:]):  # 입차 시간의 '분'이 출차 시간의 '분'보다 큰 경우
        time = (int(out_time[:2]) - int(in_time[:2]) - 1) * 60 + int(out_time[3:]) + (60 - int(in_time[3:]))
    else:
        time = (int(out_time[:2]) - int(in_time[:2])) * 60 + int(out_time[3:]) - int(in_time[3:])
    return time


def solution(fees, records):
    inout_dict = {}
    time_dict = {}
    # 1. 입/출차 기록 저장
    for record in records:
        time, car_num, situation = record.split(' ')
        if situation == 'IN':  # 입차 기록이면
            inout_dict[car_num] = time
        else:  # 출차 기록이면
            if car_num not in time_dict:  # 누적된 시간이 없다면
                time_dict[car_num] = calc_time(inout_dict[car_num], time)
            else:
                time_dict[car_num] += calc_time(inout_dict[car_num], time)

            inout_dict[car_num] = '-1'  # 입/출차 관련 기록 했으면, 지우기

    # 2. OUT 기록이 없는 경우에 대해서, 계산해주기
    for car_num in inout_dict.keys():
        if inout_dict[car_num] != '-1':
            if car_num not in time_dict:  # 누적된 시간이 없다면
                time_dict[car_num] = calc_time(inout_dict[car_num], "23:59")
            else:
                time_dict[car_num] += calc_time(inout_dict[car_num], "23:59")
        inout_dict[car_num] = []  # 입/출차 관련 기록 했으면, 지우기

    # 3. 주차요금 계산
    res = []
    for item in time_dict.items():
        car_num = item[0]
        time = item[1]

        fee = 0
        time -= fees[0]
        if time <= 0:  # 기본 요금만 계산해도 된다면
            fee = fees[1]
        else:  # 단위 요금 발생한다면
            fee = fees[1] + math.ceil(time / fees[2]) * fees[3]
        res.append((item[0], fee))  # (차량번호, 요금) 순으로 저장

    res.sort()  # '차량번호' 순으로 오름차순 정렬

    # 4. 오름차순으로 정렬된 res에 대해, 주차요금 넣고, 돌려주기
    answer = []
    for element in res:
        answer.append(element[1])

    return answer

'''
    [Review]
    이렇게 풀어서, "맞았습니다" 판정 받긴 했는데, 이러한 유형들이 기업 코테에서 요즘 자주 보여서 정리해 놓는다
    -> 문자열 시간 차이를 계산할 때는 반드시 '분 단위'로 변환해야 코드가 깔끔해진다
    -> 이와 관련해서 'YYYY-MM-DD' 계산하는 것도 그런 식으로 변환하는게 깔끔하므로, 참고하자
'''