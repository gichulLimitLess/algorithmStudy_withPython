# 실전 문제 2 - 성적이 낮은 순서로 학생 출력하기 (180페이지)
# 성적 기준으로 오름차순 정렬하면 되는 문제

N = int(input())
info_list = []
for _ in range(N): # 입력 받기
  name, score = input().split(' ')
  info_list.append((name, int(score)))

def grade(info): # 성적 기준으로 정렬할 것임, key를 성적으로 잡자
  return info[1]

info_list.sort(key=grade) # 성적 기준으로 오름차순 정렬 (이거, 더 간단하게 람다 함수 표현으로 key 설정해도 된다.)

for info in info_list: # info_list 순회하면서 학생 이름 하나씩 출력할 것임
  print(info[0], end=' ')