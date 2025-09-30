# 이중 우선순위 큐
# 데이터를 삭제하는 연산에서, 우선순위 높은 것 / 우선순위 낮은 것 -> 삭제하는 연산이 2가지임
import heapq

tc = int(input())
for _ in range(tc): # 테스트 케이스 갯수만큼 반복
  k = int(input()) # 연산 갯수
  max_heap = []
  min_heap = []
  isVisible = {} # max, min heap 동기화를 위해.. 삭제 되었는지 여부 판단
  uid = 0

  for _ in range(k):
    operation, data = input().split()
    if operation == 'I': # 삽입하는 거라면
      heapq.heappush(max_heap, (-int(data), uid)) # 우선순위에 따라서 넣는다 (-> 여긴 최대 힙 기준)
      heapq.heappush(min_heap, (int(data), uid)) # 여긴 최소 힙 기준
      isVisible[uid] = True # 있다고 표시
      uid += 1 # uid +1
    elif operation == 'D': # 삭제하는 거라면
      if len(min_heap) == 0 or len(max_heap) == 0: # queue가 비어 있을 땐
        continue # 해당 연산 무시
      if data == '-1': # 최솟값을 삭제해야 한다면
        while min_heap and not isVisible[min_heap[0][1]]: # lazy-deletion
          heapq.heappop(min_heap)
        if min_heap:
          isVisible[min_heap[0][1]] = False # 동일한 값에 대해, 모두 따로 처리해야 하므로, uid로 관리해야 한다
          heapq.heappop(min_heap)
      
      if data == '1': # 최댓값을 삭제해야 한다면
        while max_heap and not isVisible[max_heap[0][1]]:
          heapq.heappop(max_heap)
        if max_heap:
          isVisible[max_heap[0][1]] = False
          heapq.heappop(max_heap)

  # 출력 전 정리
  while min_heap and not isVisible[min_heap[0][1]]:
    heapq.heappop(min_heap)
  while max_heap and not isVisible[max_heap[0][1]]:
    heapq.heappop(max_heap)
      
  if not min_heap or not max_heap: # 비어있지 않다면
    print("EMPTY")
  else:
    print(-max_heap[0][0], min_heap[0][0])

# ========= 오답노트 ==========
# heapq는 정렬 상태를 보장하지 않음, 그리고 queue에서 그냥 pop을 하게 되면 힙 성질을 깨트릴 수 있다.
# 동일한 값이 들어올 수 있다는 것을 고려하지 않음 (-> uid로 관리해야 함)
# 그럼에도 불구하고, heapq를 사용해서 삽입한 각 list의 "맨 앞"은 우선순위가 가장 높은 친구가 와있는 건 보장되어 있다.