# 올림픽
'''
    보통 아래와 같은 규칙에 따라 어느 나라가 더 잘했는지 결정
    - 금메달 수가 더 많은 나라
    - 금메달 수가 같으면, 은메달 수가 더 많은 나라
    - 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라
    ---> 각 국가의 금/은/동메달 정보 입력 받아서, 어느 국가 몇 등했나 구해보아라
    ---> 유의할 점: 공동 등수가 발생할 경우, 그 뒤는 공동의 인원수 만큼 뒤로 미뤄진다 (ex. 공동 2등이 3명이면, 그 뒤는 5등)
'''
# 국가의 수 n, 등수를 알고 싶은 국가 k
n, k = map(int, input().split())
countries = []
for _ in range(n):
    c_num, g, s, b = map(int, input().split())
    countries.append((c_num, g, s, b))
countries.sort(key=lambda x: (-x[1], -x[2], -x[3])) # 문제 조건에 맞게 정렬

def is_same(a, b):
    if a[1] != b[1]: # 금메달 개수 다르면
        return False
    elif a[2] != b[2]: # 은메달 개수 다르면
        return False
    elif a[3] != b[3]: # 동메달 개수 다르면
        return False
    return True

def find():
    rank = 1
    acc = 1
    for i in range(n-1): # 나라들 모두 살펴보면서
        if countries[i][0] == k: # 찾는 곳이면
            print(rank)
            return
        if not is_same(countries[i], countries[i+1]): # 둘이 등수가 다르면
            rank += acc
            acc = 1
        else:
            acc += 1
    # 마지막 확인 (누락된 경우 해결)
    print(rank)

find()