# 실전 문제 4 - 효율적인 화폐 구성
# 1 <= N <= 100 (화폐 종류 갯수 N), 1 <= M <= 10000 (화폐 가치의 합 M)
# 화폐 갯수를 최소한으로 해야 함


# ======== 오답 노트 ==========
# 기존의 큰 금액부터 작은 금액까지 확인하는 그리디 방식 적용 X (배수가 아니어서.., 이러면.. 완탐 돌려야 하는데, 그러면 X -> DP 레츠고)

# 정수 N, M 입력받기
n, m = map(int, input().split())

# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
  array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

# DP 진행 (Bottom-up)
d[0] = 0
for i in range(n):
  for j in range(array[i], m+1):
    if d[j-array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
      d[j] = min(d[j], d[j-array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
  print(-1)
else:
  print(d[m])