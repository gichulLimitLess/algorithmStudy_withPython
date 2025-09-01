# 빈도 정렬
# 계수 정렬 같은 방법 쓰면.. 바로 메모리 4GB 먹어버림 -> 개에바
# 빈도 세는데.. 각 원소에 대해서 세야 하고.. 그것을 매칭? 와 이거 딕셔너리 ㄹㅇ

N, C = map(int, input().split())
num_list = list(map(int, input().split()))
count_dict = {}

for element in num_list: # num_list 하나씩 뒤져보면서 count 센다 (이거.. 시간 복잡도 (O(1,000)))
  if element not in count_dict: # key-value 쌍이 count_dict에 없다면 (not in 연산 시간 복잡도: O(1))
    count_dict[element] = 1 # 하나 새로 만들고
  else: # 이미 key-value 쌍이 있다면
    count_dict[element] += 1 # 빈도 수 +1

# 빈도 수는 count_dict에서 value 값들임
sorted_items = sorted(count_dict.items(), reverse=True, key=lambda info: info[1]) # 빈도 순으로 오름차순 정렬

for item in sorted_items: # 정렬된 것의 앞부분 값들 출력, 그것이 빈도 정렬된 값들이다
  appear_cnt = item[1] # 빈도 수 뽑아내기
  for _ in range(appear_cnt): # 빈도 수 만큼 출력하기
    print(item[0], end=' ')