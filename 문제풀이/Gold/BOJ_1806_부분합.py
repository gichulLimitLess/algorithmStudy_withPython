# 부분합
'''
    10,000 이하의 자연수로 이루어진 길이 N짜리 수열 -> 연속된 수들의 부분합 중에 그 합이 S이상 되는 것 중, 가장 짧은 것의 길이?
    10 <= n < 10만 / 0 < S <= 1억
    --> n이 최대 10만이라면, O(N) 혹은 O(NlogN) 정도로 해결해야 하는데.. O(N)으로 해결하는 방법이 있을까? --> DP로 풀 수 있지 않을까?
    --> i번째 수까지 중에서, 부분합의 크기가 S 이상인 것 중 가장 최소 길이를 "누적"해 갈 수 있을 것 같다 (왜냐면, 단방향이거든)
    --> dp[i]: num_list[:i+1]라는 부분 수열에서, 부분합의 크기가 S 이상인 것 중 가장 최소 길이
    --> 연속된 부분수열의 부분합이니까.. 약간 '투포인터'도 가미해서 풀면 좋지 않을까?
    --> 작은 예제들(테스트 케이스)을 통해 패턴을 파악해 내고, 그걸로 점화식을 세워보자!!
'''

start = 0
end = 1
sum = 0

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = 1 if num_list[0] >= s else 0 # 초기값 설정: num_list의 맨 첫번째 항이 이미 s 이상이면 길이 1짜리 부분합 있는 거고, 아니면 0임
sum += num_list[0] # sum도 초기에 한 번 더해 놓는다

while end <= len(num_list)-1: # end 포인터가 num_list의 끄트머리를 넘어가기 전까지 반복 --> O(2N)
    sum += num_list[end]
    if sum < s: # sum이 s보다 작은 동안에는
        dp[end] = dp[end-1]
    else: # sum이 s보다 크거나 같다면
        while sum >= s: # sum이 s보다 크거나 같을 동안 start를 증가 시켜서, 부분합이 s를 만족 시키는 연속된 수열의 최소 길이를 특정한다
            sum -= num_list[start]
            start += 1
        # 여기로 빠져 나왔을 땐 sum이 s보다 작은 경우임 (start가 1번 더 오른쪽으로 간 경우 --> 왼쪽으로 1칸 복원해 주어야 함)
        start -= 1
        sum += num_list[start]
        # 지금 측정한 연속 수열의 길이, i-1번째까지의 부분수열 중에서 최소 길이 중 더 긴 애로 dp[end]를 일단 누적해 간다
        # 발견했는데 0으로 계속 마킹되는 거 방지하기 위해, 조건을 걸어둠 (dp의 이전 항이 0이 아닌 경우에만 min 비교 진행)
        dp[end] = min(dp[end-1], end-start+1) if dp[end-1] != 0 else end-start+1

    end += 1 # end +1 해주면서 이어 나간다

print(dp[n-1]) # 최소 길이 출력 --> 불가능하다면 자동으로 여기엔 0이 저장되어 있을 것임