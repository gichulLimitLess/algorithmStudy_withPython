# 정렬된 배열에서 특정 수의 개수 구하기
# 특정 원소로 시작하는, 그리고 끝나는 target_start / target_end 지점을 찾아야 함!

def find_start(num_list, target):
  start = 0
  end = len(num_list) - 1

  while start <= end: # start가 end를 넘어서지 않는 상황에서만
    mid = (start + end) // 2 # mid를 구한다
    if num_list[mid] == target: # 목표 값을 찾았다면
      if mid == 0: # 맨 첫번째 구간이면 -> 여기가 시작점임 그냥
        return mid
      elif num_list[mid-1] < target: # 시작점 발견
        return mid
      else: # 그 값이긴 한데, 시작점이 아니라면, 시작점을 찾으러 가야 한다
        end = mid - 1
    elif num_list[mid] > target:
      end = mid - 1
    elif num_list[mid] < target:
      start = mid + 1
  
  return -1

def find_end(num_list, target):
  start = 0
  end = len(num_list) - 1

  while start <= end: # start가 end를 넘어서지 않는 상황에서만
    mid = (start + end) // 2 # mid를 구한다
    if num_list[mid] == target: # 목표 값을 찾았다면
      if mid == len(num_list)-1: # 맨 끝 구간이면 -> 여기가 끝점임 그냥
        return mid
      elif num_list[mid+1] > target: # 끝점 발견
        return mid
      else: # 그 값이긴 한데, 끝점이 아니라면, 끝점을 찾으러 가야 한다
        start = mid + 1
    elif num_list[mid] > target:
      end = mid - 1
    elif num_list[mid] < target:
      start = mid + 1
  
  return -1

n, x = map(int, input().split())
num_list = list(map(int, input().split()))
start_point = find_start(num_list, x)
end_point = find_end(num_list, x)

if start_point == -1 or end_point == -1: # 못 찾았다면
  print(-1)
else:
  print(end_point-start_point+1) # 결과 출력

'''
  참고사항
  -> 위와 같은 방법은, 이진 탐색을 요구하는 고난이도 문제에서 자주 사용 가능한 테크닉으로, 이러한 소스코드 잘 이해해두면 좋을 듯!
  -> 위와 같은 문제에서.. bisect_left, bisect_right 모듈을 쓰면 훨씬 간단하게 해결도 가능함
  -> 시험에서는 구현 실수(인덱스 처리, 조건 누락 등)을 줄이기 위해 bisect 사용이 권장됨
'''