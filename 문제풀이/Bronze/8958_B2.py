# OX 퀴즈
tc = int(input())

for _ in range(tc): # 테스트 케이스 갯수만큼 반복
  input_val = input()
  total = 0
  now_score = 0

  for e in input_val: # 입력으로 들어온 값들 확인하면서 for문 돌기
    if e == 'O': # 문제가 맞았다면
      now_score += 1
      total += now_score
    elif e == 'X': # 문제가 틀렸다면
      now_score = 0

  print(total) # 점수 출력