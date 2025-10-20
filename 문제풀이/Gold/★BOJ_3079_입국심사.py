# 입국 심사
'''
    [문제 조건]
    친구 총 m명 (1 <= m <= 10억)
    입국심사대 총 n개 (1 <= n <= 10만)
    k번 심사대에 앉아있는 심사관이 한 명 심사하는데 Tk(1 <= Tk <= 10억)

    걸리는 "최소 시간"이라는 것은 결국, Tk를 이루고 있는 수들 중 최소 1개 이상의 수의 "배수"가 될 수밖에 없음
    각 Tk를 현재 searching 중인 값이랑 나누고, 그것의 "몫" 값을 모조리 더했을 때, 현재 m이랑 같거나 크다면, 그 값이 "최소 시간 후보"임
    (-> 주어진 테케를 통해 해당 사실 확인 / 이거 검색해 보니까.. "단조 증가 함수" 어쩌구 문제라고 하더라..)
    특정 searching 중인 값을 일일이 찾는 것은 분명 시간 초과 날 것임 -> "파라메트릭 서치"를 활용하자
'''

n, m = map(int, input().split())
gate_times = []
for _ in range(n): # 각 심사대에서 심사를 하는데 걸리는 시간 주입
    gate_times.append(int(input()))

min_time = 10**18
start = 1
end = 10**18 # 최대 시간은 10억 * 10억 = 10^18
while start <= end: # 이거 해봐야.. O(log10^18) -> O(100)도 안됨
    mid = (start + end) // 2
    total = 0
    for gate in gate_times: # gate_times 일일이 탐색 -> O(10만)
        total += (mid // gate)

    if total >= m: # 현재 계산 값(== mid 시간 안에 처리 가능한 최대 인원수)이 m(친구 수)보다 크거나 같다면
        min_time = mid # 최소 일단 갱신
        end = mid - 1 # 혹시나.. 더 작은 게 있나 찾아본다
    else: # 현재 계산 값이 m(친구 수)보다 작다면
        start = mid + 1 # -> 더 큰 값을 찾아봐야 한다

print(min_time) # 상근이와 친구들이 심사를 마치는데 걸리는 시간의 최소 출력