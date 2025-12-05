# 파도반 수열
'''
    규칙성 찾기 문제인 것으로 판단
'''
p = [0,1,1,1,2,2,3,4,5,7,9]
# 하나씩 순서대로 채워 나가기 --> n은 최대 100
for i in range(10, 100):
    a = p[i] + p[i-4]
    p.append(a)

t = int(input())
for _ in range(t):
    c = int(input())
    print(p[c])
