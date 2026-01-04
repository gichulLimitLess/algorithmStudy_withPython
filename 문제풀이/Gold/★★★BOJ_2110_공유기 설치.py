# 공유기 설치
'''
    파라메트릭 서치 유형에 익숙해져야 한다.
    --> 해당 문제는, 그러한 유형의 대표격이 되는 문제이니, 여기서 접근한 방법을 잘 익혀두자
'''
import sys

input = sys.stdin.readline
# 집의 개수 n, 공유기의 개수 c
n, c = map(int, input().split())
wifis = [] # 공유기 위치들을 저장한 곳
for _ in range(n):
    wifis.append(int(input()))
wifis.sort() # 파라메트릭 서치를 위해 우선 오름차순 정렬 --> O(20만*log20만)

# 내가 구해야 할 것: '가장 인접한 두 공유기 사이의 거리를 최대로 하기' --> 이것을 타겟 삼아서 구하자
start = 1
end = wifis[-1] - wifis[0]
result = 0
while start <= end:
    mid = (start+end) // 2
    value = wifis[0]
    count = 1
    # 현재의 mid 값을 이용해서 공유기 설치
    for i in range(1, n): # 앞에서부터 차근차근 설치
        if wifis[i] >= value + mid:
            value = wifis[i]
            count += 1

    # 현재 mid 기준으로 설치된 공유기 개수가 목표치(c)에 도달하지 못했다면 --> 간격을 더 줄여봐야 함
    if count < c:
        end = mid - 1
    else: # 현재 mid 기준으로 설치된 공유기 개수가 목표치(c)에 도달했거나, 더 많은 경우 --> 간격을 늘려봐야 함 + 결과값 저장
        result = mid
        start = mid + 1

# 결과 출력
print(result)