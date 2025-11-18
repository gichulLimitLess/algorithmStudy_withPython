# 사전 순 최대 공통 부분 수열
'''
    [사고과정]
    - 양의 정수로만 이루어진 길이가 각각 N, M인 수열 A, B
        --> 1 <= N <= 100, 1 <= M <= 100
    - 모든 부분집합을 다 구해서, 일일이 대조하려면.. 2^100 * 2 ==> 말도 안되니까 당연히 DP로 해결해야 함
    - 그런데, 중요한 건.. 단순히 최장 공통 부분 수열을 구하는 게 아니라..
        '사전 순으로 가장 나중인 공통 부분 수열'을 구해야 한다
    - 이는.. 우선 기존의 '최장 공통 부분 수열'을 구하는 것처럼 구하고..
        백트래킹으로 '최장 공통 부분 수열'이 무엇인지 뽑아낸다
        그런 다음, '최장 공통 부분 수열'에서, 원소 중 가장 큰 값을 뽑고,
        가장 큰 값을 뽑은 인덱스로부터 그 뒤의 부분 수열 중 또 가장 큰 값을 뽑고.. 이걸 반복한다
        언제까지? 뒤에 부분 수열의 값이 0이 될 때까지!
'''
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# 1. 2차원 dp 테이블을 활용해서, 우선 '최장 공통 부분 수열의 길이'를 구하기
# dp[i][j] = 수열 a에서 i+1번째 원소까지, 수열 b에서 j+1번째 원소까지 고려했을 때, 최장 공통 부분 수열의 길이
dp = [[0 for _ in range(m)] for _ in range(n)]

# dp 배열 초기값 설정 (-> 1행과 1열은 초기화해야 함)
dp[0][0] = 1 if a[0] == b[0] else 0
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + 1 if a[0] == b[j] else dp[0][j-1]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + 1 if a[i] == b[0] else dp[i-1][0]

# dp 테이블 채워 나가기 --> O(10000)
for i in range(1, n):
    for j in range(1, m):
        if a[i] == b[j]: # 서로 원소 값이 같다면
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

if dp[i-1][j-1] == 0: # k == 0이라면
    print(0)
else:
    # 2. dp 배열을 "백트래킹" 하면서, '최장 공통 부분 수열'을 구하기 --> O(100)s
    i = n-1
    j = m-1
    res = []
    while i > 0 and j > 0: # 행, 또는 열의 맨 끝에 갈 때까지 진행
        if a[i] == b[j]: # 비교했던 곳이, 원소가 같았다면 --> 원소 추가하고, 대각선 방향으로 올라간다
            res.append(a[i])
            i -= 1
            j -= 1
        else:
            if dp[i][j-1] > dp[i-1][j]: # dp 테이블에서 '왼쪽'의 수가 더 큰 경우
                j -= 1
            else:
                i -= 1

    if i == 0: # 맨 위 '행'에 도달했을 경우
        while i >= 0 and j >= 0: # 행을 하나씩 감소시켜 보면서 찾는다
            if a[i] == b[j]:
                res.append(a[i])
                i -= 1
                j -= 1
            else:
                j -= 1
    elif j == 0: # 맨 왼쪽 '열'에 도달했을 경우
        while i >= 0 and j >= 0: # 행을 하나씩 감소시켜 보면서 찾는다
            if a[i] == b[j]:
                res.append(a[i])
                i -= 1
                j -= 1
            else:
                i -= 1

    res.reverse() # '백트래킹'을 통해서 찾은 것은, 뒤집어야 원래 순서대로 저장되어 있다

    # 3. '최장 공통 부분 수열'에서, 원소 중 가장 큰 값을 뽑고,
    # --> 가장 큰 값을 뽑은 인덱스로부터 그 뒤의 부분 수열 중 또 가장 큰 값을 뽑고.. 이걸 반복한다
    part_arr = res
    ans = []
    while len(part_arr) > 0:  # 언제까지? 뒤에 부분 수열의 값이 0이 될 때까지! --> 약 O(101*100//2)
        max_idx = -1
        max_val = 0
        for i in range(len(part_arr)):
            if max_val < part_arr[i]: # 부분 수열에서, 더 큰 애가 있다면, 계속 갱신해야 함
                max_idx = i
                max_val = part_arr[i]
        ans.append(max_val) # 부분 수열 중 가장 큰 친구 저장
        part_arr = part_arr[max_idx+1:] # max 뒤쪽에서 가장 큰 거 계속 갱신

    # 정답 출력
    print(len(ans))
    for e in ans:
        print(e, end=' ')