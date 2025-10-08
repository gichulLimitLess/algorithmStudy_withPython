# A+B-C
# 첫줄에는 A, B, C를 수로 생각했을 때의 A+B-C의 값 출력
a = int(input())
b = int(input())
c = int(input())

print(a+b-c)

# 둘째 줄에는 A,B,C를 "문자열"로 생각했을 때의 A+B-C의 값 출력
print(int(str(a)+str(b))-c)