# 고정점 찾기 (-> O(logN)으로 알고리즘 설계해야 함 - 이진탐색 조질게요)
# --> 1 <= n <= 100만
n = int(input())
num_list = list(map(int, input().split()))

start = 0
end = len(num_list)-1

def find_fixedPoint(num_list, start, end):
    while start <= end: # start가 end보다 작거나 같은 경우일 때만 반복
        mid = (start + end) // 2 # 가운데 인덱스
        if num_list[mid] == mid: # "고정점"을 찾았다면
            return mid

        if num_list[mid] < mid: # 고정점이 mid보다 오른쪽에 있는 경우임
            start = mid + 1
        elif num_list[mid] > mid: # 고정점은 mid보다 왼쪽에 있는 경우임
            end = mid - 1

    return -1 # 못 찾았으면 -1 return

print(find_fixedPoint(num_list, start, end)) # 출력