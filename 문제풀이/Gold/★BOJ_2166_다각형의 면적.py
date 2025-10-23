# 다각형의 면적
# ---> 삼각형으로 일일이 쪼개는 방법도 생각해 봤으나, 훨씬 좋은 방법이 있음: "신발끈 공식"

n = int(input())
# x, y 좌표들 저장하는 배열 선언
x_list = []
y_list = []

for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

# "신발끈 공식" 적용
def shoelace_formula():
    res1 = 0
    res2 = 0
    for i in range(n):
        res1 += x_list[i%n] * y_list[(i+1)%n] # x1*y2 + ... + xn*y1 구현
        res2 += x_list[(i+1)%n] * y_list[i%n] # x2*y1 + ... + x1*yn 구현

    # res1에서 res2를 뺀 값에 절댓값을 취해주고, 그것을 2로 나누면 된다
    # --> 소수 둘째자리에서 반올림하여, 첫째자리까지 표현
    res = round((abs(res1 - res2)/2), 1)
    return res

print(shoelace_formula()) # 결과 출력