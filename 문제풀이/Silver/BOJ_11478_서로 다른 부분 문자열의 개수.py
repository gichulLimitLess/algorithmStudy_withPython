# 서로 다른 부분 문자열의 개수
'''
    문자열의 최대 길이는 1000
    -> O(N^3)의 알고리즘까지도 OK
'''
s = input()
substrings = set() # 서로 다른 것의 부분 문자열 세기 위해, 여기에 저장

# 여기서.. O(N^3) 소요
for length in range(1, len(s)+1):
    for start in range(len(s)-length+1):
        # 여기서 O(N) 소모 --> 그치만, 슬라이싱 연산은 C 레벨의 메모리 복사 연산이라 다른거에 비해 매우 빠름
        substrings.add(s[start:start+length])

print(len(substrings)) # 서로 다른 부분 문자열 개수 출력