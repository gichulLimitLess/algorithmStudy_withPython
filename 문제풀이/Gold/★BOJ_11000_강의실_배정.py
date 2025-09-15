# 강의실 배정 - '그리디' 연습하겠다고 풀어제낄 문제
# 수업의 끝 시간 기준으로 오름차순 정렬한다
# 그리고, 현재 시간이 이전 수업 시간의 끝보다 크거나 같은 경우, 강의실은 필요가 없다
# --> 이거 비교만 계속 하고, 이전 시간(prev) 갱신만 하면 된다

# import sys
# input = sys.stdin.readline

# n = int(input()) # 1 <= N <= 20만
# class_list = [] # 수업들의 정보가 들어가 있는 list

# for _ in range(n): # 수업 정보 입력받기
#   start, end = map(int, input().split())
#   class_list.append((start, end))

# class_list.sort(key=lambda x:(x[1], x[0])) # 2번째 원소 기준으로 오름차순 정렬
# length_val = len(class_list)

# classroom_cnt = 1
# prev = class_list[0][1]

# for i in range(1, length_val):
#   if prev <= class_list[i][0]: # 강의실을 같이 쓸 수 있는 경우
#     prev = class_list[i][1]
#   else:
#     classroom_cnt += 1

# print(classroom_cnt) # 강의실 갯수 출력

# --> 강의실 여러 개의 끝나는 시간을 동시에 추적하지 않고,하나(prev)만 관리한 것이 패착임!
# ---> 이런 경우에는.. heap을 통해서 현재 열려 있는 모든 강의실의 종료 시간을 추적해야 함

# ========== 정답 코드는 아래와 같다 =============
import heapq
n = int(input())

q = []

for i in range(n):
  start, end = map(int, input().split())
  q.append((start, end))

q.sort()

room = []
heapq.heappush(room, q[0][1]) # 끝 시간을 넣어준다

for i in range(1, n):
  if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작이 빠르면
    heapq.heappush(room, q[i][1]) # 새로운 회의실 개설 --> 다른 방에서 해야 함
  else:
    heapq.heappop(room) # 새로운 회의로 시간 변경 위해 pop후 새 시간 push
    heapq.heappush(room, q[i][1])

print(len(room)) # 남아있는 회의 갯수가 결국 필요한 최소 강의실 갯수