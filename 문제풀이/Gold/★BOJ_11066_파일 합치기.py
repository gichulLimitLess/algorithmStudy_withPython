# 파일 합치기
'''
    [사고과정]
    - 일일이 완전탐색을 하는 경우에는 답 없는데... 어떻게 함? 그래프인데 이거 뭔데..
'''
# [BOJ 11066] 파일 합치기
# https://www.acmicpc.net/problem/11066

import sys
input = sys.stdin.readline

T = int(input().strip())  # 테스트 케이스 수

for _ in range(T):
    K = int(input().strip())  # 파일의 개수
    files = list(map(int, input().split()))

    # prefix_sum[i] = 0번째부터 i번째 파일까지의 누적 크기 합
    prefix_sum = [0] * (K + 1)
    for i in range(1, K + 1):
        prefix_sum[i] = prefix_sum[i - 1] + files[i - 1]

    # dp[i][j] = i번째 파일부터 j번째 파일까지 합치는 최소 비용
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    # 구간 길이를 2부터 K까지 점점 늘려가며 계산
    # (파일 하나만 있는 구간은 합칠 필요가 없으므로 비용 = 0)
    for size in range(2, K + 1):  # size = 구간의 길이 (2개 파일부터 시작)
        for start in range(1, K - size + 2):  # 시작 인덱스
            end = start + size - 1            # 끝 인덱스
            dp[start][end] = float('inf')     # 일단 큰 값으로 초기화

            # [start, end] 구간을 k를 기준으로 왼쪽/오른쪽으로 나누어본다.
            # 각 분할점 k에 대해:
            #   - 왼쪽 구간: dp[start][k]
            #   - 오른쪽 구간: dp[k+1][end]
            #   - 두 구간을 합칠 때 드는 비용 = prefix_sum[end] - prefix_sum[start - 1]
            for k in range(start, end):
                cost = dp[start][k] + dp[k + 1][end] + (prefix_sum[end] - prefix_sum[start - 1])
                dp[start][end] = min(dp[start][end], cost)

    # 최종적으로 [1, K] 구간의 최소 비용이 정답
    print(dp[1][K])
