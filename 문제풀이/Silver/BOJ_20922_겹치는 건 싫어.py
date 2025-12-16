# 겹치는 건 싫어
'''
    [사고과정]
    뭔가, 이거는 '연속 수열' 관한 것이고, 수열의 최대 길이가 20만 이하..
    O(N), 아니면 O(NlogN) 안에 처리해야 할 텐데.. 여기서 떠오르는 건.. 투포인터?
'''
n, k = map(int, input().split())
n_list = list(map(int, input().split()))
count_dict = dict() # 원소 갯수를 세기 위한 dict
s = 0
count_dict[n_list[s]] = 1
max_len = 0 # '최장 연속 부분 수열'의 길이

# 하나씩 쭉 세기 --> O(20만 * 2)
for i in range(1, n):
    if n_list[i] not in count_dict: # 한 번도 등장한 적이 없는 원소라면
        count_dict[n_list[i]] = 1
    else: # 등장한 적이 있다면
        count_dict[n_list[i]] += 1

    if count_dict[n_list[i]] > k: # 현재 수열이 같은 정수를 k개 초과한 경우
        while count_dict[n_list[i]] > k: # k개 이하가 될 때까지 s 증가
            count_dict[n_list[s]] -= 1
            s += 1
    max_len = max(max_len, i-s+1) # 최대 갱신

print(max_len) # 결과 출력