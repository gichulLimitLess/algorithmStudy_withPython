# List of Unique Numbers
'''
    [사고 과정]
    - 우선, 길이가 N인 전체 수열에서, 길이가 i인 연속된 수열의 개수: (N-i+1)개
        --> 즉, N이 최대 10만인 조건에서는.. 연속된 수열의 전체 개수는.. 최대 약 50억 개가 나올 수 있다.
    - 절대 완전탐색으로는 불가능하다. 그러면 dp?
        -> 근데 dp는 선형적으로 계속 누적되어 가는 형태에서만 가능한데, 여기가 그런 느낌은 아닌데..
    - 특정 구간에서 겹치지 않는 것을 구하기.. 뭔가 "투포인터"의 냄새가 난다
'''
n = int(input())
num_list = list(map(int, input().split()))

start = 0
total = 0 # 경우의 수 저장하는 변수
seen = set()

for end in range(n): # end가 끄트머리 넘어가기 전까지 계속 수행
    while num_list[end] in seen: # 중복되는 원소가 있다면
        seen.remove(num_list[start]) # 하나씩 없애고
        start += 1 # start 하나씩 증가
    seen.add(num_list[end]) # 본 것에 추가
    total += (end - start + 1) # end가 고정되어 있을 때, 부분 수열의 개수는 end-start+1

print(total)