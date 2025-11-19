# 피보나치 수 6
'''
    [사고과정]
    기존의 피보나치 수를 푸는 가장 대표적인 방법인 dp를 그대로 사용할 경우..
    n의 최대 크기가 10^18, 배열의 크기가 가볍기 TB 단위를 넘어가기 때문에 사용할 수 없음
    --> 규칙성을 찾아서, 수학적인 접근을 해야 함
    수학적인 접근을 해야 한다는 건 알겠는데... 어떤 방식으로?
    (힌트 보고.. 이런 건 처음 봤다. "분할정복 거듭제곱")
'''
# n = int(input())
# dp = [0 for _ in range(3000)]
# dp[0] = 0
# dp[1] = 1
# for i in range(2, 3000):
#     dp[i] = (dp[i-1] + dp[i-2]) % 1000000007 # 지속적으로 1,000,000,007으로 나눈 나머지를 누적해간다
# print(dp)

import sys

input = sys.stdin.readline

MOD = 1_000_000_007


# 1. 두 행렬을 곱하는 함수
def mat_mul(A, B):
    # A, B는 2x2 행렬
    result = [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD],
    ]
    return result


# 2. 2x2 행렬 A를 n번 거듭제곱하는 함수 (분할정복)
def mat_pow(A, n):
    # 종료 조건: A^1 = A
    if n == 1:
        return A

    # 분할정복: 절반을 먼저 계산
    half = mat_pow(A, n // 2)

    # 짝수: A^(n) = half^2
    if n % 2 == 0:
        return mat_mul(half, half)

    # 홀수: A^(n) = half^2 * A
    else:
        return mat_mul(mat_mul(half, half), A)


# 3. 입력 처리
n = int(input())

# n = 0일 때 처리
if n == 0:
    print(0)
    exit()

# 기본 피보나치 변환 행렬
base_matrix = [
    [1, 1],
    [1, 0],
]

# 4. base_matrix^n 을 계산
res = mat_pow(base_matrix, n)

# 5. res[0][1] = F(n)
print(res[0][1] % MOD)
