# 영화감독 숌
n = int(input())
num = 666
count = 0
  
while True: # 그냥, 숫자 하나씩 더해가면서, 거기에 '666' 있는지 확인 때린다
  if '666' in str(num):
    count += 1
    if count == n:
      print(num)
      break
  num += 1