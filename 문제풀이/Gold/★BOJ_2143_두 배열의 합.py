# 두 배열의 합
'''
[오답노트]
파라메트릭 서치 관련한 것에 대해서 시도하다가, 또 못 풀었는데,
"A 배열 모두 탐색하며 모든 부배열의 합을 구하고, B 배열 모두 탐색하며 모든 부배열의 합 구한 다음,
T(타겟값)을 만족하는 경우를 찾는 게 핵심이다!"
-> 시간 복잡도 계산할 때, 상황이 괜찮으면 O(n^2) 써도 된다.. (-> n이 최대 1000인데.. 상관 ㄴ)
-> 정렬이 안되면, 이분탐색을 다이렉트하게 쓸 수 없다는 것을 인지해야 함 (-> 이분탐색 쓰려면.. 무조건 "정렬" 되어 있어야 함!)
-> bisect 라이브러리 활용법 제대로 이해해 두자! (bisect.bisect_left, bisect.bisect_right)
'''

# 2차 시도
# --> 원소가 음수일 수도 있고, 정렬할 수도 없고.. 이러면 일단 모든 부배열의 합을 구하는게 답인듯
target = int(input())
# A 관련 입력받기
n = int(input())
A = list(map(int, input().split()))
# B 관련 입력받기
m = int(input())
B = list(map(int, input().split()))

A_dict = {}
B_dict = {}
# 모든 부배열의 합 각각 구하기 --> O(n^2 + m^2)
for start in range(len(A)):
    sum = 0
    for i in range(start, len(A)):
        sum += A[i]
        if sum not in A_dict: # 해당 부배열 합의 값이 dict에 없다면
            A_dict[sum] = 1
        else:
            A_dict[sum] += 1
for start in range(len(B)):
    sum = 0
    for i in range(start, len(B)):
        sum += B[i]
        if sum not in B_dict: # 해당 부배열 합의 값이 dict에 없다면
            B_dict[sum] = 1
        else:
            B_dict[sum] += 1

answer = 0
for A_sumVal in A_dict: # A_dict에서 구한 합의 값을 가져와서, B의 합의 값과 매칭되는 거 있나 확인 (-> O(1000))
    if target-A_sumVal in B_dict: # 해당하는 값이 B_dict에 key로 있다면
        answer += (A_dict[A_sumVal] * B_dict[target-A_sumVal])

print(answer) # 결과 출력