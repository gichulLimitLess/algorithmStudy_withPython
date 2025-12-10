# 등수 구하기
n, new_score, p = map(int, input().split())
if n > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

# 리스트가 꽉 찼고, 새 점수가 마지막 점수보다 작거나 같으면 불간으
if n == p and scores[-1] >= new_score:
    print(-1)
else: # 해당 경우는 무조건 리스트 안에 '새로운 점수'가 들어갈 수 있는 경우
    rank = 1
    for s in scores:
        if s > new_score:
            rank += 1
        else:
            break
    print(rank)