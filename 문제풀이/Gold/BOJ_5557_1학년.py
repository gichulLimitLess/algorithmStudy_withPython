# 1학년
'''
    전체를 다 탐색할 경우.. +, - 중복순열을 모두 탐색해야 할 텐데.. 이러면 최대 2^100 -> 에바이지 않을까?
    결국 최적화 모드로 가야 하는데.. 어떤 "상태"를 정의해야 할까?
    --> 직접 "손"으로 예제를 분석해 보니,
        - 주어진 숫자 조합에서 i번째 숫자까지 계산
        - 값이 j가 되는 경우의 수
        --> 이렇게 2가지 "상태"로 나누면 좋을 것 같다는 생각이 들었다
    --> dp 점화식 정의:
        dp[i][j] = num_list(주어진 숫자 배열)에서 i번째 숫자까지 계산했을 때, 값이 j가 되는 경우의 수 (0<=j<=20)
        초기 dp 배열은 INF로 정의 (INF는 해당 경우가 "없다"는 것을 의미)
        그리고, dp배열의 첫째 행은 미리 초기값으로 계산해 놓아야 한다
    --> dp 전이 정의:
        dp[i][j] = dp[i-1][j-num_list[i]] + dp[i-1][j+num_list[i]]
        (단,
            1 <= i <= n-2
            0 <= j-num_list[i], j+num_list[i]
            dp[i-1][j-num_list[i]], dp[i-1][j+num_list[i]]이 각각 INF가 아닐 때만 해당 값에 반영
        )
'''
n = int(input())
num_list = list(map(int, input().split()))
# [참고사항] DP에서는 보통 "0"을 없음의 상태로 처리한다

# (n-1) * 21 크기 dp 배열 선언
# --> 숫자 배열의 n번째 항은 "결과"를 의미하기에 여기에서 고려할 필요 X
dp = [[0 for _ in range(21)] for _ in range(n-1)]

# dp 배열 첫째 항 초기화
for j in range(21):
    dp[0][j] = 1 if j == num_list[0] else 0

# dp 배열 채워 나가기
# --> 해당 시간 복잡도는 O(n*21) ==> 해봐야 O(21000) --> 매우 Good
for i in range(1, n-1):
    for j in range(21):
        res = 0
        if 0 <= j-num_list[i] <= 20: # '+' 연산 해서 여기로 올 수 있는 경우 check
            res += dp[i-1][j-num_list[i]]
        if 0 <= j+num_list[i] <= 20: # '-' 연산 해서 여기로 올 수 있는 경우 check
            res += dp[i - 1][j + num_list[i]]
        dp[i][j] = res # 계산한 값을 그냥 dp[i][j]에 집어 넣는다

print(dp[n-2][num_list[n-1]]) # 해당 값 출력