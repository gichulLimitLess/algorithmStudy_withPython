# 바닥까지 하강
arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0,0,1], [0, 1, 0]]

print("기존")
for i in range(len(arr)):
  print(arr[i])

def gravity(arr):
  n = len(arr)
  m = len(arr[0])
  for i in range(m): # 모든 '열'에 대해서..
    write = n-1
    for j in range(n-1, -1, -1): # 밑에서부터 위로 하나씩 보면서 간다
      if arr[j][i] == 1: # 해당 칸에 요소가 있는 경우
        if write == j: # 여전히 맨 밑을 가리키고 있다면
          write -= 1
          continue
        arr[write][i], arr[j][i] = 1, 0
        write -= 1

gravity(arr)

print("변화")
for i in range(len(arr)):
  print(arr[i])