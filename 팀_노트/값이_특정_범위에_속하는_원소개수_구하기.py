# '정렬된 리스트'에서..
# --> 값이 특정 범위에 속하는 원소의 개수 구하기
# ---> bisect_left()와 bisect_right()를 적절히 활용해서 count_by_range() 함수.. 아래처럼 쉽게 구현 가능

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 갯수를 반환하는 함수 (-> 리스트는 '정렬된' 리스트여야 한다)
def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

# 리스트 선언
a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 -1 이상, 3 이하인 데이터 개수 출력
print(count_by_range(a, -1, 3))