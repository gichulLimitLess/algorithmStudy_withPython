# 팰린드롬?
# --> 팰린드롬은.. "어떤 단어를 뒤에서부터 읽어도 똑같은 단어"를 뜻한다
import sys

input = sys.stdin.readline # n이 최대 100만번 입력하는데.. 유의하자
N = int(input())
num = list(map(int, input().split()))
M = int(input())

# dp[i][j]는 index i~j가 Palindrome인지 저장
dp = [[0] * N for _ in range(N)]

# 1개짜리는 모두 Palindrome
for i in range(N):
    dp[i][i] = 1
# 2개짜리는 두 숫자가 같으면 Palindrome, 다르면 아님
for i in range(N - 1):
    if num[i] == num[i + 1]:
        dp[i][i + 1] = 1
# 3개짜리부터는 처음 숫자와 끝 숫자가 같고, 중간 값이 Palindrome이면 Palindrome
# 예를 들어, dp[0, 5]는 num[0]==num[5]이고, dp[1, 4]==1 이면 Palindrome
# dp[0][1]~dp[N-2][N-1], dp[0][2]~dp[N-3][N-1], ... 처럼 왼쪽위~오른쪽 아래로 대각선으로 순차적으로 채워나감
for k in range(2, N):
    i = 0
    j = k
    while j < N:
        if num[i] == num[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

        i += 1
        j += 1

result = []

for _ in range(M):
    S, E = map(int, input().split())
    if dp[S - 1][E - 1] == 1:
        result.append(1)
    else:
        result.append(0)

for k in result:
    print(k)