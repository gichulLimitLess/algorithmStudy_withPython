# 직각삼각형
# --> 피타고라스 정리가 만족하면 'right', 아니면 'wrong'인 것임
while True:
    lengths_list = list(map(int, input().split()))
    lengths_list.sort() # 가장 긴 변이 맨 뒤에 있을 거임
    if lengths_list[0] == 0 and lengths_list[1] == 0 and lengths_list[2] == 0: # 종료 조건
        break

    # '피타고라스 정리'를 만족하는 지 확인
    if lengths_list[2] ** 2 == lengths_list[0] ** 2 + lengths_list[1] ** 2:
        print('right')
    else:
        print('wrong')