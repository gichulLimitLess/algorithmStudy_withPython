# 팰린드롬수
while True:
    a = input()
    if a == '0': # 0이면 종료
        break

    start = 0
    end = len(a)-1
    isPelinDrome = True
    while start <= end:
        if a[start] != a[end]: # 같지 않으면, 팰린드롬 수가 아님
            isPelinDrome = False
            break
        start += 1
        end -= 1

    if isPelinDrome:
        print('yes')
    else:
        print('no')