# 곱하기 혹은 더하기
# '+'와 'x'를 사용해서 왼쪽부터 순서대로 계산할 때, 가장 큰 수 만들어 버리기
# --> '0'이랑 '1'은 'x'보다 '+'를 하는 게 무조건 이득 / '2'~'9' 사이는 무조건 'x'가 이득

str_list = list(input())
num_list = []

for element in str_list:
  num_list.append(int(element))

total = 0

for element in num_list: # 하나씩 뽑아다 쓴다
  if element <= 1 or total <= 1: # 0 또는 1이면
    total += element
  else: # 위 상황이 아니면, 무조건 곱하는 게 더 크게 됨
    total *= element

print(total)