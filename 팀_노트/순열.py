# 순열: n개 중에서 중복없이 r개를 뽑음, 이때 순서 상관있음
# --> 순열은 순서가 다르고 원소가 같으면 다른 걸로 침

arr = [1,3,4,6,7,8]
visited = [False for _ in range(len(arr))] # 방문 여부를 저장할 것임
result = [] # 순열 값들을 저장할 배열

def permutations(depth, r, permu):
  if depth == r: # r개만큼 모두 다 뽑았을 경우
    result.append(permu) # 결과에 순열 결과 넣기
    return # 여기서 더 이상 탐색하지 않고 재귀 호출 종료
  for i in range(len(arr)): # arr의 길이만큼 순회
    if visited[i]: # 이미 방문한 곳이면, 건너뜀
      continue
    
    visited[i] = True # 방문 표시
    permutations(depth+1, r, permu + [arr[i]]) # 재귀 호출
    visited[i] = False # 방문 표시 해제

permutations(0, 3, []) # 순열 뽑기
print(result) # 순열 결과 출력