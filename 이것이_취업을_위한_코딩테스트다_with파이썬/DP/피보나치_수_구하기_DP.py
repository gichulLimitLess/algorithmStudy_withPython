# 메모이제이션 기법을 사용해서 피보나치 수 구하기 문제를 해결한 소스 코드

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
memo = [0] * 100

# 피보나치 함수를 재귀함수로 구현(Top-down Dynamic Programming)
def fibo(x):
	# 종료 조건(1 혹은 2일 때 1을 반환)
	if x == 1 or x == 2:
		return 1
	
	# 이미 계산한 적 있는 문제라면 그대로 반환
	if memo[x] != 0:
		return memo[x]
	
	# 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
	memo[x] = fibo(x-1) + fibo(x-2)
	return memo[x]

print(fibo(99)) # 위처럼 DP를 쓰면, 99번째 피보나치 수를 구해도 금방 풀 수 있음 (중복 연산 방지하니깐!)

# ==================================================
# 위에 꺼는 Top-Down 방식이었고, 아래는 Bottom-Up 방식!
# ==================================================

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
memo = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
memo[1] = 1
memo[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현(Bottom-up Dynamic Programming)
for i in range(3, n+1):
	memo[i] = memo[i-1] + memo[i-2]

print(memo[n]) # 위처럼 DP를 쓰면, 99번째 피보나치 수를 구해도 금방 풀 수 있음 (중복 연산 방지하니깐!)