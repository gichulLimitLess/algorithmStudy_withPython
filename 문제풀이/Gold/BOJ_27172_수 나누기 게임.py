# 수 나누기 게임
'''
    [풀이과정]
    - 뭔가.. 나누어 떨어지는 느낌이 있다면.. 이거 '에라토스테네스의 체'를 이용하는 거 아닌가?
'''
# from math import sqrt
#
# n = int(input())
# x_list = list(map(int, input().split()))
#
# # --> 여기 만드는 데.. 최악의 경우 O(10만*2)
# is_Prime = [True for _ in range(max(x_list)+1)]
# num_list = [0 for _ in range(max(x_list)+1)]
#
# # x_list에 있는 숫자 개수 기록 --> O(10만)
# for x in x_list:
#     num_list[x] += 1
#
# # 에라토스테네스의 체 활용 -> 그런데, "x_list"에 존재하는 수 기준으로만!
# for i in range(1, int(sqrt(len(is_Prime)))+1):
#     if is_Prime[i] and num_list[i] > 0: # 소수이고, 0개 이상 존재하는 수여야만 함
#         r = 2
#         while i * r < len(is_Prime): # i와 배수 관계에 있는 애들은 모두 "소수 아님" 처리
#             is_Prime[i*r] = False
#             r += 1

# ------------ 아래는 정답 코드 -------------
import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().rstrip().split()))
S = set(x)           # x_list에 존재하는 수만 빠르게 판별
M = max(x)
sieve = [0] * (M+1)  # 각 숫자의 점수 변화 누적용

for i in x:
    for j in range(2*i, M+1, i):  # i의 배수들을 탐색
        if j in S:                # 실제로 존재하는 카드라면
            sieve[i] += 1         # 작은 수(i)는 +1점
            sieve[j] -= 1         # 큰 수(j)는 -1점

for i in x:
    print(sieve[i], end = ' ')

'''
    [오답노트]
    - 위 문제는 에라토스테네스의 체의 골격(배수 순회)을 가져다 쓴 거지.. 소수 판별을 직접 하는 것이 X
     ---> 난.. 지금까지 "에라토스테네스의 체 = 소수 구하는 알고리즘"으로만 인식했는데..
          정답을 내려면.. 배수를 효율적으로 순회하는 루프 구조로 일반화 했어야 했다.
     ---> 즉, 난 의미적 이해...(소수 탐색)에만 갇혀 있었고.. 구조적 이해(배수 순회)로 확장 못한 게 패착이다.
     => “나는 ‘에라토스테네스의 체’를 ‘소수를 구하는 도구’로만 봤다.
        이제는 ‘배수 관계를 효율적으로 순회하는 구조’로 일반화해서 볼 수 있어야 한다.”
'''