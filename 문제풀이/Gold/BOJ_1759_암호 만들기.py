# 암호 만들기
# --> "알파벳이 증가하는 순서"로 암호를 만들려면, 같은 요소를 뽑았을 때, 1가지만 있음 -> 조합으로 레츠고
from itertools import combinations

moeum = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, input().split())

# 가능한 암호를 사전식으로 출력해야 하므로 입력 이후에 정렬 수행
alpha_list = list(input().split(' '))
alpha_list.sort() # --> 이렇게 하면, 조합을 뽑을 때 알파벳 증가 순으로 뽑게 될거임

# 길이가 l인 암호 모두 확인
for combi in combinations(alpha_list, l): # 조합을 뽑는다
    moeum_cnt = 0
    for element in combi: # 조합 결과를 보며, 모음 갯수를 센다
        if element in moeum: # 해당 element가 모음이라면
            moeum_cnt += 1

    # 모음 갯수가 1개 이상이고, 자음의 갯수가 2개 이상이면
    if moeum_cnt >= 1 and l - moeum_cnt >= 2:
        print(''.join(combi))