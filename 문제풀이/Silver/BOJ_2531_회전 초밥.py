# 회전 초밥
'''
    2 <= 회전 초밥 벨트에 놓인 접시 수 N <= 3만
    2 <= 초밥의 가짓수 d <= 3천
    2 <= 연속해서 먹는 접시 수 k <= N <= 3천
    1 <= 쿠폰 번호 c <= d
    --> 일일이 최대 3천 개의 연속되는 접시 수를 탐색할 경우, O(3천 * 27000) => 거의 1억에 가깝기에, "슬라이딩 윈도우" 쓰면 좋을 듯
'''
n, d, k, c = map(int, input().split())
dishes = []
for _ in range(n):
    dishes.append(int(input()))
# 회전 초밥 구현을 위해 2배 확장
for i in range(n):
    dishes.append(dishes[i])

sushi = dict() # 현재 스시 갯수 저장

# 1. 초반 윈도우 갯수 세기 --> O(3천)
for i in range(k):
    if dishes[i] not in sushi: # 없으면 1
        sushi[dishes[i]] = 1
    else: # 있으면 기존 꺼에 +1
        sushi[dishes[i]] += 1
# 쿠폰 확인
if c not in sushi:
    sushi[c] = 1
else:
    sushi[c] += 1
max_sushi_cnt = len(sushi) # 우선 이걸로 "최대 스시 종류 갯수" 저장

# 2. 윈도우를 하나씩 옆으로 옮겨가며 진행 --> O(2*2만 7천)
start = 0
end = k-1
while start < n-1:
    # 시작 포인터 증가
    sushi[dishes[start]] -= 1
    if sushi[dishes[start]] == 0: # 해당 윈도우에서 특정 종류의 스시가 모두 사라졌다면
        del sushi[dishes[start]]
    start += 1
    # 끝 포인터 증가
    end += 1
    if dishes[end] not in sushi: # 없으면 1
        sushi[dishes[end]] = 1
    else:  # 있으면 기존 꺼에 +1
        sushi[dishes[end]] += 1
    # max_sushi_cnt 필요하면 갱신
    max_sushi_cnt = max(len(sushi), max_sushi_cnt)

# 결과 출력
print(max_sushi_cnt)