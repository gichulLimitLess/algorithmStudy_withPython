# 카드 정렬하기
# 카드 묶음의 크기가 작은 순부터 오름차순 정렬을 한다
# --> 현재 국소 최적이 전체 최적을 만든다는 아이디어.. greedy

import heapq

n = int(input())
num_list = []

for _ in range(n):
  num_list.append(int(input()))

total = 0
num_list.sort() # 오름차순으로 우선 정렬해 놓는다
while len(num_list) != 1: # num_list의 길이가 1이 아닐 때까지 반복
  a = heapq.heappop(num_list) # 우선순위 1순위를 빼낸다
  b = heapq.heappop(num_list) # 우선순위 2순위를 빼낸다
  res = a + b
  total += res # total에 넣어 놓는다
  heapq.heappush(num_list, res) # 더한 값을 넣어 놓는다

print(total) # 결과 출력

'''
  ========== 오답노트 ===========
  -> 동적으로 데이터가 과정에 다시 들어와서 변화가 생긴다면..
  -> 우선순위 큐, 세그먼트 트리 등 동적 자료구조가 필요할 가능성이 높다!
'''