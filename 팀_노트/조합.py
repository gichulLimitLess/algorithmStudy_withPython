# 조합: n개 중에서 중복없이 r개를 뽑음, 이때 순서 상관없음
# --> 조합은 순서가 다르고 원소가 같으면 같은 걸로 침

# 조합에서는 visited 배열 필요 없음 -> start 인덱스를 이동시켜 중복 방지
arr = [1,3,4,6,7,8]
result = [] # 조합 값들을 저장할 배열

def combinations(depth, start, r, combi):
  if depth == r: # r개를 다 뽑았으면
    result.append(combi) # 조합 구한 것들 결과에 저장
    return # 그냥 돌려준다
  
  for i in range(start, len(arr)): # start부터 순회
    combinations(depth+1, i+1, r, combi + [arr[i]]) # i+1로 다음 시작점 이동

combinations(0, 0, 3, []) # 조합 함수 수행
print(result) # 결과 출력