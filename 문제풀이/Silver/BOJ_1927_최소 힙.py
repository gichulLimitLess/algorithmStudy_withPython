# 최소 힙
import heapq # --> 참고: Python에서는 기본적으로 최소 힙을 지원

n = int(input()) # 연산의 개수 n
queue = []
for _ in range(n):
    x = int(input()) # 입력 받기
    if x == 0: # --> 가장 작은 값 출력하고, 그 값을 배열에서 제거하는 경우
        if len(queue) == 0: # 비어있는 경우엔
            print(0)
        else: # 뭐라도 있으면, 빼낸다
            print(heapq.heappop(queue))
    else: # --> x라는 값을 추가하는 연산 수행
        heapq.heappush(queue, x)
