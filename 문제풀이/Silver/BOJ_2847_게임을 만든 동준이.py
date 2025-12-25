# 게임을 만든 동준이
'''
    거꾸로 확인하며 그리디로 처리하면 될 듯 하다
'''
INF = int(1e9)

n = int(input())
score_list = []
for _ in range(n):
    score_list.append(int(input()))

ans = 0
prev = INF
for i in range(n-1, -1, -1):
    if prev <= score_list[i]: # 이전 꺼가 지금 지금꺼보다 작거나 같은 경우 --> 빼줘야 한다
        ans += (score_list[i] - prev + 1)
        prev = prev - 1
    else:
        prev = score_list[i]

print(ans) # 이것이, 점수를 몇 번 감소시키면 되는지에 대한 답