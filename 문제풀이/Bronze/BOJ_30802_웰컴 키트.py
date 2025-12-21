# 웰컴 키트
import sys

input = sys.stdin.readline

# 참가자 수
N = int(input().strip())

# 사이즈별 티셔츠 신청자 수 (6가지)
sizes = list(map(int, input().split()))

# 티셔츠 묶음 단위 T, 펜 묶음 단위 P
T, P = map(int, input().split())

# 티셔츠 묶음 최소 주문 수
shirt_bundles = 0
for s in sizes:
    # size에 신청자가 있다면 (0도 가능하지만 계산은 올림)
    # 올림: (s + T - 1) // T 로도 할 수 있음
    shirt_bundles += (s + T - 1) // T

# 펜 묶음 최대 주문 수와 나머지
pen_bundles = N // P
pen_left = N % P

# 출력
print(shirt_bundles)
print(pen_bundles, pen_left)
