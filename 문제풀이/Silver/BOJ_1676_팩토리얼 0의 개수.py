# 팩토리얼 0의 개수
n = int(input()) # n
memo = [0 for _ in range(n+1)] # 팩토리얼 계산 효율적으로 하기 위해.. dp 사용

now = 0
for i in range(n+1):
  if i == 0 or i == 1:
    memo[i] = 1
  else:
    memo[i] = memo[i-1] * i

res_str = str(memo[n]) # 처음으로 0이 아닌 숫자가 나오기 전까지의 0의 개수 알아보기 위해, 문자열로 바꾼다
cnt = 0
for i in range(len(res_str)-1, -1, -1): # 뒤에서부터 탐색
  if res_str[i] != '0': # 0이 아닌 거 발견하면, 바로 0 갯수 출력하고 break
    print(cnt)
    break
  else:
    cnt += 1