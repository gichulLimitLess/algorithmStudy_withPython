# 먹을 것인가 먹힐 것인가
'''
    일일이 쌍을 비교해서 큰지 작은지를 비교하면.. 최악의 경우 O(2만*2만) -> O(4억)
        --> 1초 안에 문제를 풀 수 없음
    그러나, B를 오름차순 정렬한 후, A를 기준으로, 현재 선택된 원소보다 작은 원소가 B에 있으면, 그만큼의 갯수를 더해주는 방식으로 가면 되지 않을까?
        --> 이진 탐색 (bisect_left 모듈 활용)하면, O(2만 * log2만)으로 해결 가능!
'''
from bisect import bisect_left

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split()) # a의 수 n, b의 수 m
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # B를 오름차순 정렬 --> O(2만 * log2만)
    B.sort()
    # A의 원소를 하나씩 훑어가며, B에 들어갈 수 있는 위치를 bisect_left로 찾는다
    # (해당 결과로 나온 인덱스 값)은, 자기보다 작은 원소 개수를 의미 --> 그게 결국 쌍을 이루는 값임
    # 시간 복잡도: O(2만 * log2만)
    cnt = 0
    for e in A:
        cnt += bisect_left(B, e)
    print(cnt) # 결과 출력