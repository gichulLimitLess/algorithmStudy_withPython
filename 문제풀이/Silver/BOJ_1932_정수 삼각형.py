# 정수 삼각형
n = int(input()) # n의 최대 크기 500 --> 2^500 버틸 수 없으니.. dp로 풀자
triangle = [] # 삼각형 정의

for _ in range(n): # 삼각형 입력 받기
    row = list(map(int, input().split()))
    triangle.append(row)

for i in range(1, n): # 정수 삼각형 합이 최대가 되는 것을 각 자리에 저장
    for j in range(len(triangle[i])):
        left = triangle[i-1][j-1] if j-1 >= 0 else 0
        right = triangle[i-1][j] if j < len(triangle[i-1]) else 0
        triangle[i][j] = max(left, right) + triangle[i][j] # 현재 위치의 최댓값을 갱신하며 내려간다

print(max(triangle[n-1])) # 최댓값 출력