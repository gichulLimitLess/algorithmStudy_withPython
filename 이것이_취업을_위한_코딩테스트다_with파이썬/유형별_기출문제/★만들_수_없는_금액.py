# 만들 수 없는 금액
# 작은 것부터 하나씩 확인하면서.. 양의 정수를 늘려가면서 확인해보면 될 듯

target = 1

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort() # 오름차순 정렬

# target을 1로 잡고, 지금 있는 숫자들로 target을 만들 수 있는지 차근차근 올라가며 점검한다
for element in num_list:
  if target < element:
    break
  target += element

print(target) # target에 저장되어 있는 값이, 결국 만들 수 없는 양의 정수 최솟값이 된다
