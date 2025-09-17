# 주식
# --> 이거 그리디로 풀어야 하는 것 같은데.. 그러면 "매 상황마다 좋다고 생각되는 것만 취한다"
import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    profit = 0

    # 뒤에서부터 확인
    for i in range(n-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            profit += max_price - prices[i]

    print(profit)


# --- 오답노트----
# 앞에서부터 보게 되면.. 언제 살 지 결정 못하고, 뒤에서부터 보면 언제 팔지만에 대해서..
# 정할 수 있으니까... 아주 간단하게 해결이 가능하다
# 순차적으로 보는 게 에바라고 생각 된다면... 반대로 돌려보는 것도 한 번 생각해 봐라!