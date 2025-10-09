# 소수 구하기
# --> 입력의 크기를 보니까, "에라토스테네스의 체"를 이용해야 할 듯
import math

m, n = map(int, input().split())

pn = [True for i in range(n+1)] # 0과 1은 판단에서 제외할 것임
pn[1] = False # 1은 소수가 아님

for i in range(2, int(math.sqrt(n))+1): # 끝까지 안 봐도 됨 (-> 대칭성이 있기에..)
    if pn[i] == True:
        j = 2 # 곱할 배수 (i를 제외한 모든 수 지우기)
        while i*j <= n: # n 까지 배수인 것들 다 쳐낸다
            pn[i*j] = False
            j += 1

# 결과 출력
for i in range(m, n+1):
    if pn[i]: # '소수'인 것이 True라면, 아니면, 출력하지 않는다
        print(i)