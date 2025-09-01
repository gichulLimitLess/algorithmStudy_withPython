# 실전 문제 1 - 위에서 아래로 (178페이지)
# 내림차순 정렬을 위해 필요한 sort 함수의 옵션과 공백 기준 출력 방법만 알면 쉽게 풀 수 있는 문제임

N = int(input())
num_list = []
for _ in range(N): # 배열의 수 입력 받기
  num_list.append(int(input()))

num_list.sort(reverse=True) # 'reverse' 옵션을 통해 내림차순 정렬 가능! (기본은 오름차순임)
for element in num_list: # 결과 출력
  print(element, end=' ')