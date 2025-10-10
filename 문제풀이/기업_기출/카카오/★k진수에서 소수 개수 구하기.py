# k진수에서 소수 개수 구하기
# 이 코드는 프로그래머스에서 돌아가는 거라, 거기서 돌려야 정상 동작함!
import math

# k진수로, 수를 변환하는 함수
def zinbub_change(num, k):
    res = []
    while num >= k:  # num이 k보다 크거나 같을 동안만 아래 프로세스를 반복
        a = num % k
        num //= k
        res.append(str(a))
    res.append(str(num))  # 지금 남은 num 값은 맨 head이다
    res.reverse()  # 뒤집어야 완성된다
    return ''.join(res)


# 소수를 찾는 함수 (-> 여기선, 에라토스테네스의 체 활용하면 메모리 터지거나, 시간 초과 날수도..)
def is_prime(num):
    # 엣지 케이스 처리
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:  # 나누어 진다면
            return False
    return True


def solution(n, k):
    changed_num = zinbub_change(n, k)  # 반환된 것은 changed_num에 저장 (문자열 형태)
    num_list = [int(x) for x in changed_num.split('0') if x != '']  # '0' 기준으로 모두 분해 (빈 문자열은 스킵하도록 로직 구성)

    # 소수 갯수 찾기 및 결과 반환
    answer = 0
    for element in num_list:
        if is_prime(element):  # 소수로 판별되면
            answer += 1
    return answer