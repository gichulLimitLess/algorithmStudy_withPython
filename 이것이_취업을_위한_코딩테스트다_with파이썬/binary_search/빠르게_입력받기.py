# 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편
# input() 함수를 그대로 사용하면, 동작 속도가 느려서 시간 초과로 오답 판정 받을수도 있음
# 그에 대한 해결책으로 readline()을 사용해보자

import sys

# 하나의 문자열 데이터 입력받기
# readline() 사용할 땐, rstrip() 꼭 호출해야 함, Enter(공백 문자) 제거해야 합니다.
input_data = sys.stdin.readline().rstrip()

# 입력 받은 문자 그대로 출력
print(input_data)