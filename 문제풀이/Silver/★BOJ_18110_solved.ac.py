# solved.ac
'''
    '절사평균'이라는 내용이 중요
        -> 제외되는 사람 수는 위, 아래에서 각각 반올림
    계산되는 평균 또한 정수로 반올림
'''
from decimal import Decimal
import sys
input = sys.stdin.readline

'''
    파이썬에서 사사오입을 가장 간단하게 구현하는 꼼수
    ==> 0.5를 더한 뒤, int()로 소수점 올려버리면 됨
'''
def custom_round(val):
    return int(val + 0.5)

n = int(input()) # 난이도 의견 개수 n (0 ≤ n ≤ 3 × 10^5)

if n == 0:
    print(0)
else:
    op_list = []
    for _ in range(n):
        op_list.append(int(input()))

    op_list.sort()

    # 절사 인원 수 계산
    except_cnt = custom_round(n * 0.15)

    # 슬라이싱으로 합계 계산
    # except_cnt가 0일 경우 인덱싱 에러 방지를 위한 처리 필요할 수 있으나
    # 슬라이싱은 범위 벗어나도 에러 안남
    trimmed_list = op_list[except_cnt: n - except_cnt]

    # 최종 평균 계산
    print(custom_round(sum(trimmed_list) / len(trimmed_list)))


