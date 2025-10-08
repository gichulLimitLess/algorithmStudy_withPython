# ACM 호텔
# 지문은 좀 길고 복잡했는데, 간단히 생각해보면, 단순한 계산문제임
# --> 초반에, 모든 방이 비어있다고 가정했으므로, H를 나눈 몫, 나머지 값을 활용하면 될 듯

tc = int(input())
for _ in range(tc):
    h, w, n = map(int, input().split()) # h: 호텔의 충 수/ w: 각 층의 방 수 / n: 몇 번째 손님
    back = 1 + ((n-1) // h) # 뒤에 XX 부분은 이렇게 계산됨
    back_num = ''
    if len(str(back)) == 1:
        back_num = str(0) + str(back)
    else:
        back_num = str(back)
    front = 1 + ((n-1) % h) # 앞에 YY 부분은 이렇게 계산됨
    print(str(front) + str(back_num))