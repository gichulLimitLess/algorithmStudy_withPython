# 좌표 압축
'''
    자기 밑에 몇 개의 수가 있는지를 세야 한다
    --> 이거 일일이 비교해서 개수 세려고 하면.. O(100만^2)
        => 시간 당연이 터지니까.. 이럴 때 사용할 수 있는 것이 우선순위 큐 (최소 힙)
'''
import heapq
n = int(input())
n_list = list(map(int, input().split()))
q = []
infos = dict() # key: 특정 수 / value: 자기 밑에 몇개의 수가 있는가

# 1. 우선 우선순위 큐에 다 담는다 -> 가장 최소값이 pop 시에 먼저 나올 것이다 (O(100만*log100만))
for n in n_list:
    heapq.heappush(q, n)

# 2. 하나씩 꺼내며 dict에 자기 밑에 몇개 있는지 저장 --> (O(100만*log100만))
cnt = 0
while q:
    now = heapq.heappop(q)
    if now not in infos: # 이미 있는 값이 아니어야 함 --> "중복 방지"
        infos[now] = cnt
        cnt += 1

# 3. 다시 n_list 돌면서 결과 출력 --> O(100만)
for n in n_list:
    print(infos[n], end=' ')

# =================== 위처럼 풀어도 답 맞긴 하지만, 아래처럼 푸는게 정석임 ===================
# 좌표 압축 - 정석 풀이

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 1. 중복 제거 + 정렬
sorted_unique = sorted(set(arr))

# 2. 값 -> 순위(인덱스) 매핑
rank = {value: idx for idx, value in enumerate(sorted_unique)}

# 3. 원본 순서대로 출력
print(' '.join(str(rank[x]) for x in arr))