# 용액
'''
    전체 용액의 수 n: 2 <= n < 10만
    n개의 정수에서.. 각 정수의 범위: -10억 이상, 10억 이하
    --> 우선, 전체 용액의 수가 10만이면.. O(N)으로 해결할 수 있는 방법을 생각해 봐야 함
    --> start = 0, end = len(용액 리스트)-1로 두고, 투포인터를 생각해볼 수 있지 않을까?
'''
n = int(input())
num_list = list(map(int, input().split())) # 해당 리스트는 정렬된 상태로 주어짐

start = 0
end = len(num_list)-1
min_sum = int(1e9*2 + 1) # 일단, 가능한 최대 합은 문제 제약 조건에 따라 20억이므로, 20억+1 해준다
min_pair = [-1, -1]

'''
    아래와 같이 풀이하면
        - 모든 원소가 알칼리성인 경우
        - 모든 원소가 산성인 경우
        - 둘이 섞인 경우
        --> 모두 풀이 가능 / O(n)의 시간에 말이다
'''
while start < end: # start가 end와 겹치거나 역전하기 전까지 반복
    res = num_list[end] + num_list[start]
    # ============ 아래 주석처리 되어 있는 코드는 "오답 코드" ===============
    # if abs(res) < min_sum: # 현재 최소 합보다 더 작은 합이 나왔다면
    #     min_pair[0], min_pair[1] = num_list[start], num_list[end]
    #     min_sum = abs(res) # 최소 갱신 --> 절댓값으로 갱신
    #     end += 1 # 더 작은 값으로 줄여, 혹시 합이 더 0에 가까운 것이 있나 찾는다
    # else: # 현재 최소 합보다 더 큰 합이라면
    #     start -= 1 # start를 더 큰 값으로 키워서, 절댓값이 0에 가까운 애를 찾아봐야 한다

    if abs(res) < min_sum: # 현재 최소 합보다 더 작은 합이 나왔다면
        min_sum = abs(res) # 최소 합 갱신 ---> '절댓값'으로 갱신
        min_pair = [num_list[start], num_list[end]]

    if res < 0: # 계산한 값이 음수라면
        start += 1 # 더 0에 가깝게 만들기 위해서 start를 증가 시켜야 함
    else: # 계산한 값이 양수 또는 0이라면
        end -= 1 # 더 0에 가깝게 만들기 위해서 end를 감소 시켜야 함

print(min_pair[0], min_pair[1]) # 결과 출력