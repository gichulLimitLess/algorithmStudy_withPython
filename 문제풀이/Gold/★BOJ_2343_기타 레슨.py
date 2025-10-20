'''
    [기타 레슨]
    n개의 강의 (강의 순서 바꿀 수 없음) & m개의 블루레이에 모든 기타 강의 녹화
    -> m개의 블루레이 크기를 최소 (m개의 블루레이는 모두 같은 크기여야 함)
    -> 1 <= n <= 10만, 1 <= m <= n, 각 강의는 10000분을 넘지 않으니, 모든 강의 시간의 합은 최대 10억을 넘지 않는다

    [사고 과정]
    n개의 강의에 대한 정보는 순서가 바뀌면 안된다. 그런데, m개의 그룹에 대해서 최소를 찾는 것을 완전탐색하면 절대 안될 것 같다 (시간 터질 듯)
    "블루레이 크기"를 타겟으로 잡고, 파라메트릭 서치를 하면 되지 않을까? 하는 생각을 해봤다.
    start = 1, end = 10억(->O(log10억))으로 잡아두고.. n개의 강의를 순차 탐색(-> O(10만))해 보면서, mid 값을 넘어갈 때마다 group 개수를 count,
        -> 그룹 개수가 m보다 작으면, 블루레이 크기가 과도하게 큰 것이니까 end = mid - 1
        -> 그룹 개수가 m보다 크면, 블루레이 크기가 과도하게 작은 것이니까 start = mid + 1
        -> 그룹 개수가 m개가 되었다면, min_val = min(min_val, mid) 하고, 여기서 더 최소를 찾아야 하므로, end = mid - 1
    총 걸리는 시간은 아마.. O(10만) * O(log10억) = 약 O(320만)? -> 충분히 2초 안에 통과 가능하지 않을까 싶다
'''
n, m = map(int, input().split())
l_list = list(map(int, input().split())) # 기타 강의 길이들
INF = int(1e9)
min_val = INF # 일단 최소 값은 10억으로 설정

start = 1 # 최소 1 (-> 모든 수는 자연수니까..)
end = INF # 최대 10억

while start <= end: # 블루레이 최소 크기를 타겟으로 한 "파라메트릭 서치" 시작
    mid = (start+end) // 2
    total = 0
    group_cnt = 1 # 그룹은 무조건 최소 1개는 존재함
    for lecture in l_list: # 기타 강의들에서 개수 세기 -> 강의 순서 바뀌면 안되므로, 순차 탐색 해야 함
        if lecture > mid:  # ✅ 핵심: 단일 강의가 mid보다 크면 불가능
            group_cnt = m + 1  # -> 강제 실패 처리
            break
        if total + lecture > mid: # mid보다 큰 경우 -> 현재 lecture를 더해 그룹을 만들 수 없음
            group_cnt += 1
            total = lecture
        else: # 아직은 그룹 구성 요소 추가할 수 있음 -> total에 lecture를 계속 더해 나간다
            total += lecture

    # m개 이하면 (-> m개 안되는 경우 포함) --> 최소 갱신하고, 더 작은 값을 찾으러 간다
    # (이러다 보면..어느 순간 group_cnt가 m보다 커지는 순간이 오니까 상관 X)
    if group_cnt <= m:
        min_val = mid
        end = mid - 1 # 더 작은 거 찾으러 나선다
    else: # m개보다 group_cnt가 많다면, 더 큰 거 찾으러 가야 한다
        start = mid + 1 # 더 큰 거 찾으러 나선다

print(min_val) # 가능한 블루레이 크기 중 최소 출력