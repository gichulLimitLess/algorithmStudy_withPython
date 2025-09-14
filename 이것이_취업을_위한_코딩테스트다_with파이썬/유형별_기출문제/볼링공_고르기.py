# 볼링공 고르기
# 조합과 dict을 적절히 사용하면 될 것 같은 문제

from itertools import combinations

n, m = map(int, input().split())
ball_list = list(map(int, input().split())) # 볼링공 무게 입력받기

dict = {}
for element in ball_list: 
  if dict.get(element) == None:
    dict[element] = 1
  else:
    dict[element] += 1

num_list = []
for element in dict.keys(): # dict의 key들을 하나씩 돌아가며 탐색
  num_list.append(element)

cnt = 0
for element in combinations(num_list, 2): # 하나씩 돌아가면서 탐색
  cnt += (dict[element[0]] * dict[element[1]]) # 경우의 수를 곱해서 더해간다

print(cnt) # 경우의 수 출력

# 시간 복잡도 해봐야.. O(N + M + M!) 정도..? 입출력 포함한다 해도, 1초 안엔 충분히 될 듯