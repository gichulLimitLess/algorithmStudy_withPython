# 실전 문제 2 - 개미 전사
# 3 <= N <= 100, 0 <= K <= 1000
# 모든 경우의 수 다 따지려 들잖아...? 개에바임, DP로 풀어야 함
N = int(input()) # 식량창고의 갯수 N
storage_list = list(map(int, input().split())) # 식량 창고 정보

memo = [0] * N

# 초기값들 설정해야 함
memo[0] = storage_list[0]
memo[1] = max(storage_list[0], storage_list[1])

# 아래에서부터 점화식으로 조지기
for i in range(2, N):
  memo[i] = max(storage_list[i-1], storage_list[i-2] + storage_list[i])

# memo가 다 채워졌다면, 여기에서 최댓값을 뽑아내면 됨
print(max(memo))

# ======= 오답 노트 =========
# DP는.. 점화식을 똑바로 세워야 한다!
# 위 문제에서는.. "현재 칸 선택을 했을 때, 안했을 때..", 2가지 선택지를 반드시 고려해야 함