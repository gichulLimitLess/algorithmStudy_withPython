# 실전 문제 1 - 큰 수의 법칙 (92페이지)
# 길이 N인 배열, 주어진 수들을 M번 더해서 가장 큰 수 만드는 법칙, 특정 인덱스의 수를 K번 초과해서 더할 수는 X

# N, M, K = map(int, input().split(' '))
# num_list = list(map(int, input().split(' ')))

# # 가장 큰 수를 만들려면, 무조건 가장 큰 수들을 더해야 한다
# # 오름차순 정렬하고, 맨 뒤쪽에 있는 수(가장 큰 수)를 K번씩 더하고, 두번째로 큰 수 한 번 더해주고, 다시 맨 뒤에 있는 수 K번 더하고.. 이런 식으로 하면 가장 큰 수 구하기 가능
# num_list.sort() # 오름차순 정렬

# answer = 0 
# cnt = 0

# for _ in range(M): # 총 M번 더해야 한다
#   if cnt < K: # K번보다 덜 더해졌을 경우
#     answer += num_list[-1]
#     cnt += 1
#   elif cnt == K: # K번 더했을 경우
#     answer += num_list[-2] # 두 번째로 큰 수 한 번 더해준다
#     cnt = 0 # 연속 횟수 초기화

# print(answer)

# M이 100억을 넘어가면.. 위처럼 하게 되면 시간 초과 on
# 반복되는 수열이 있다는 것을 알아채고, 더 간단하게 구하는 방법도 있다
N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()

answer = 0
cnt = 0

set_res = (num_list[-1] * K + num_list[-2]) * (M//(K+1))
remainder = num_list[-1] * (M % (K+1))

print(set_res + remainder)