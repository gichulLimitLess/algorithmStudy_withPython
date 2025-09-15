# 럭키 스트레이트
# 반을 쪼개서 각각의 자릿수 합 확인하면 되는 그리 안 어려운 문제임

input_str = input()
length_val = len(input_str)

total_left = 0
total_right = 0

for i in range(length_val // 2): # 왼쪽 자릿수 합 출력
  total_left += int(input_str[i])

for i in range(length_val//2, length_val): # 오른쪽 자릿수 합 출력
  total_right += int(input_str[i])

if total_left == total_right:
  print("LUCKY")
else:
  print("READY")