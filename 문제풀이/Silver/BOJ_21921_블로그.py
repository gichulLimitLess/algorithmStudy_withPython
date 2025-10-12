# 블로그
n, x = map(int, input().split())
num_list = list(map(int, input().split()))

# 길이가 고정된 투 포인터 (== 슬라이딩 윈도우) 기법을 쓰면 될 듯
start = 0
end = x - 1
sum_val = sum(num_list[start:end+1])
sumVal_dict = {} # sum한 부분집합 합의 값 갯수들 모두 저장
max_val = 0 # 최대 값
cnt = 0

while end <= n-1: # end가 num_list 범위 벗어나기 전까지
    max_val = max(max_val, sum_val) # 최댓값 갱신
    if sum_val in sumVal_dict:
        sumVal_dict[sum_val] += 1
    else:
        sumVal_dict[sum_val] = 1
    sum_val -= num_list[start]
    start += 1
    end += 1
    sum_val += (num_list[end] if end != n else 0) # 마지막 부분 엣지 케이스 처리

if max_val == 0: # 갱신되지 않았다면 (-> 최대가 0이라면..)
    print("SAD")
else: # 갯수 출력
    print(max_val)
    print(sumVal_dict[max_val])