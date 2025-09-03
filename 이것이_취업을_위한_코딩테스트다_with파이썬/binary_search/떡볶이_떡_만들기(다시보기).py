# 실전 문제 2 - 떡볶이 떡 만들기
# 1 <= N <= 1,000,000 (떡 개수)
# 1 <= M <= 20억 (요청한 떡 길이)
# 0 <= (절단기 설정 높이) <= 10억

# 참고: 코딩 테스트나 프로그래밍 대회에서는 보통 파라메트릭 서치 유형은 이진 탐색을 이용하여 해결
# -> 일반적으로 파라메트릭 서치 문제 유형은 이진 탐색을 재귀적으로 구현하지 않고 반복문을 통해 구현하면 더 간결하게 풀 수 있음

# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split(' ')))

# 각 떡의 개별 높이 정보를 입력 받기
riceCake_lenList = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(riceCake_lenList)

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2

  for x in riceCake_lenList:
    if x > mid: # mid 값이 x보다 작을 때만 빼자 (그래야 양수 나오잖아)
      total += x - mid
  
  # 자르고 나서 떡의 양(total)이 필요한 양보다 작은 경우, 더 많이 잘라야 한다 -> 왼쪽 탐색
  if total < m:
    end = mid - 1
  # 자르고 나서 떡의 양(total)이 필요한 양보다 많은 경우, 덜 잘라야 한다 -> 오른쪽 탐색
  else:
    result = mid # 최대한 덜 잘랐을 때가 정답이니깐, 여기에서 result로 우선 기록 (계속 갱신되다가 정답 될거임)
    start = mid + 1

# 정답 출력
print(result)

