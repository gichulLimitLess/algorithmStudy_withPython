# 안테나
# --> 집에다가 안테나를 설치, 동일한 위치에 여러 집 존재 가능
# --> 안테나로부터 모든 집까지의 거리 총 합이 최소가 되도록
# 해결법? 오름차순으로 정렬해서, 가운데에 있는 친구를 선택하면 될 듯
# --> len(house_list) // 2 하면.. mid에서 가장 작은 값으로 출력됨

n = int(input()) # 집의 수 n개
house_list = list(map(int, input().split()))

house_list.sort() # 오름차순 정렬
if len(house_list) % 2 == 0: # 길이가 짝수라면
  idx = len(house_list) // 2 - 1 # 더 작은 애를 출력해야 하므로, 인덱스 -1 해야 함
else: # 홀수면 
  idx = len(house_list) // 2

print(house_list[idx]) # 이게 그냥 정답임