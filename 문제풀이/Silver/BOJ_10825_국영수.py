# 국영수
n = int(input()) # 학생 수 n
student_list = []
for _ in range(n):
  name, score_1, score_2, score_3 = input().split() # 입력
  student_list.append((name, int(score_1), int(score_2), int(score_3))) # (학생 이름, 국어, 영어, 수학) 순

# 국어 점수 내림차순, 영어 점수 오름차순, 수학 점수 내림차순, 이름 사전 순 오름차순
student_list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 결과 출력
for element in student_list:
  print(element[0])