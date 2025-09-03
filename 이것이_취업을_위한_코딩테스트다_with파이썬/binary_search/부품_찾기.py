# 실전 문제 1 - 부품 찾기
# 1 <= N <= 1,000,000
# 1 <= M <= 100,000
# N 크기의 배열을 M번 탐색해서 찾아야 하니.. 사이즈가 장난 아님 -> 이건 "이진 탐색"의 향기가 난다

import sys

N = int(input())
num_list = list(map(int, sys.stdin.readline().rstrip().split())) # N 크기의 배열

M = int(input())
check_list = list(map(int, sys.stdin.readline().rstrip().split())) # M 크기의 배열

def binary_search(target): # 이진 탐색하는 함수
  start = 0
  end = len(num_list) - 1
  
  while start <= end: # start가 end랑 만나거나 역전되기 전까지 반복
    mid = (start + end) // 2
    if num_list[mid] == target: # 찾았다면
      return 'yes'
    elif num_list[mid] < target: # element보다 중간점이 작다면 -> mid 기준 오른쪽 탐색
      start = mid + 1
    else: # element보다 중간점이 크다면 -> mid 기준 왼쪽 탐색
      end = mid - 1
  
  return 'no' # 여기까지 왔으면 못 찾은거임

for element in check_list: # check_list 훑어가면서 하나씩 출력
  print(binary_search(element), end=' ')

# 이 문제에서는 계수 정렬의 개념이나, 단순히 특정한 수가 한 번이라도 등장했는지 검사하면 되므로.. 집합(set) 자료형을 이용해서 해결도 가능