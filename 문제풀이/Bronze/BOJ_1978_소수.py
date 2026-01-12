N = int(input())
nums = list(map(int, input().split()))

count = 0
for num in nums:
    # 2 이상만 소수 가능
    if num > 1:
        is_prime = True
        # 2부터 num - 1까지 나누어 떨어지는지 검사
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

print(count)