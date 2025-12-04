# 카드 구매하기
'''
    [사고과정]
    처음엔 좀 헷갈렸으나.. 생각해보면 dp로 계속 누적해가면 될 것 같은 문제
    dp[i] -> 카드 i개를 사기 위한, 지불하는 금액의 최대
'''
n = int(input())
cards = list(map(int, input().split())) # cards[i] -> 카드 i개 들어있는 카드팩 가격
cards = [0] + cards

dp = [0 for _ in range(n+1)]
for idx, card in enumerate(cards):
    dp[idx] = card

for i in range(2, len(cards)):
    for j in range(1, i):
        dp[i] = max(dp[i-j]+cards[j], dp[i])

print(dp[n]) # 결과 출력