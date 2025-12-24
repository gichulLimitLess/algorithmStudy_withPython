# 시리얼 번호
'''
    [사고과정] -> 정렬방법
    1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
    2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
    3. 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
'''
n = int(input())
s_numbers = [] # 시리얼 번호들
for _ in range(n):
    s_numbers.append(input())

# sumVal은 각 시리얼 넘버에 대해 모든 자리수 합을 저장한 dict
sumVal = dict()
for s in s_numbers:
    sumVal[s] = 0
    for e in s:
        if '0' <= e <= '9':
            sumVal[s] += int(e)

# 위에 명시되어 있는 기준으로 정렬
s_numbers.sort(key=lambda x: (len(x), sumVal[x], x))
# 출력
for s in s_numbers:
    print(s)