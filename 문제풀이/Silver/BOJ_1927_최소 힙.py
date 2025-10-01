# 최소 힙
import heapq # --> 참고: Python에서는 기본적으로 최소 힙을 지원
import sys

input = sys.stdin.readline

n = int(input()) # 연산의 개수 n
queue = []
answers = []
for _ in range(n):
    x = int(input()) # 입력 받기
    if x == 0: # --> 가장 작은 값 출력하고, 그 값을 배열에서 제거하는 경우
        if len(queue) == 0: # 비어있는 경우엔
            answers.append(0)
        else: # 뭐라도 있으면, 빼낸다
            answers.append(heapq.heappop(queue))
    else: # --> x라는 값을 추가하는 연산 수행
        heapq.heappush(queue, x)

for answer in answers: # 정답 출력
    print(answer)