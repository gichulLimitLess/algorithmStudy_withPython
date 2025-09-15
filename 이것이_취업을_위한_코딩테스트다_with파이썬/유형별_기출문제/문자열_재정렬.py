# 문자열 재정렬
# 숫자 값이랑 문자 값 따로 처리해 주면 될 듯

input_val = input()

alphabet_list = []
total = 0

for e in input_val: # 문자열 보면서 그게 문자인지 숫자인지 확인
  if ord(e) >= ord('A') and ord(e) <= ord('Z'): # 알파벳 대문자라면
    alphabet_list.append(e)
  else: # 숫자라면
    total += int(e)

alphabet_list.sort() # 문자 기준으로 오름차순 정렬
print(''.join(alphabet_list), end='')
print(total)