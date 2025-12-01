# 나무 자르기
'''
    나무의 수 N (1 <= N <= 100만)
    상근이가 집으로 가져가려는 나무 길이 M (1 <= M <= 20억)
    Q. 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최대?
    --> 수가 매우 큰 문제 / 대표적인 '파라메트릭 서치' 유형이라 판단됨
'''
n, m = map(int, input().split())
trees = list(map(int, input().split()))

# [0, 나무들의 길이 최댓값] 가지고 파라메트릭 서치 시작
start = 0
end = max(trees)
ans = 0

# 절단기에 설정할 수 있는 높이의 최댓값 찾으러 가기 --> O(100만 * log20억)
while start <= end:
    mid = (start+end) // 2
    total = 0
    # 나무 하나씩 봐가면서 total 누적 --> O(100만)
    for tree in trees:
        if tree > mid: # 나무 길이가 자르려고 하는 타겟값(mid)보다 더 길이서 자를 수 있을때만 누적
            total += (tree-mid)

    if total >= m: # 적어도 m미터를 가져갈 수 있다면
        ans = max(ans, mid)
        start = mid+1 # start를 갱신 시키고 다시 찾아본다 (--> 더 큰 ans 값을 찾으러 가본다)
    else: # m미터를 못 가져간다면
        end = mid-1 # end를 갱신 시키고 다시 찾아본다 (--> 더 작은 값을 찾으러 가본다)

print(ans) # 결과 출력