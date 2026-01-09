# 좌표 정렬하기 2
n = int(input())
coordinates = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))
coordinates.sort(key=lambda x: (x[1], x[0])) # y좌표, x좌표 증가하는 순으로

for x, y in coordinates:
    print(x, y)
