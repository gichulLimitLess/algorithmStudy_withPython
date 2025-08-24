# 실전 문제 2 - 숫자 카드 게임
# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임 (단, 룰을 지켜야 함)
N, M = map(int, input().split())

# 배열 입력 받기 & 오름차순 정렬
card_list = []
for _ in range(N):
  row = list(map(int, input().split()))
  row.sort() # 오름차순 정렬
  card_list.append(row)

# card_list 하나씩 돌아가며 각 row에서 제일 작은 거 고르기, 그것을 현재 제일 크다고 판단되는 것(answer)과 비교
answer = 0
for row in card_list:
  answer = max(answer, row[0])

print(answer) # 답 출력

# Tip: 그냥 각 행에 대해서 min 함수 써서, 찾아도 될 것 같습니다 (배열에서 min/max 함수 쓰면 시간복잡도가 n이더라)