# 리스트 회전
def rotated_90(a):
  n = len(a) # 기존(a)의 세로
  m = len(a[0]) # 기존(a)의 가로
  result = [[0] * n for _ in range(m)] # 배열의 가로, 세로 길이가 뒤바뀌는 것 주의
  for i in range(n): # 범위 주의
    for j in range(m): # 범위 주의
      result[j][n-i-1] = a[i][j]
  return result

def rotated_180(a):
  n = len(a)
  m = len(a[0])
  result = [[0]*m for _ in range(n)]
  for i in range(n): # 범위 주의
    for j in range(m): # 범위 주의
      result[n-i-1][m-j-1] = a[i][j]
  return result

def rotated_270(a):
  n = len(a)
  m = len(a[0])
  result = [[0] * n for _ in range(m)] # 배열의 가로, 세로 길이가 뒤바뀌는 것 주의
  for i in range(n): # 범위 주의
    for j in range(m): # 범위 주의
      result[m-1-j][i] = a[i][j]
  return result

a = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(rotated_90(a))
print(rotated_180(a))
print(rotated_270(a)) 