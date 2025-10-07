# 내려가기
n = int(input())

# 4MB라는 메모리 제한이 있다면, 갱신형 dp 테이블을 고려해야 함
# --> 이거 때문에 틀렸다.
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]

# 최대, 최소 dp 테이블을 채워야 할 때, 입력하는 족족 갱신해 준다
for i in range(n): # 내려가며 본다
    row = list(map(int, input().split()))
    # 첫 행은, 자기 자신으로 초기화 후, 아무 행동도 하지 않는다
    if i == 0:
        max_dp = row[:]
        min_dp = row[:]
        continue

    max_row = [0, 0, 0]
    min_row = [0, 0, 0]

    for j in range(3): # 옆으로 가며 본다
        a = j - 1 if j != 0 else j
        b = j
        c = j + 1 if j != 2 else j

        # 갱신형 dp 테이블을 갱신하기 위해, min_row/max_row를 갱신한다
        max_row[j] = max(max_dp[a], max_dp[b], max_dp[c]) + row[j]
        min_row[j] = min(min_dp[a], min_dp[b], min_dp[c]) + row[j]

    for k in range(3):
        max_dp[k] = max_row[k]
        min_dp[k] = min_row[k]

print(max(max_dp), min(min_dp)) # 최대/최소는 각 dp 테이블의 맨 밑 행에 저장되어 있다.