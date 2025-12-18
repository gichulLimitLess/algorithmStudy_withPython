# 가희와 키워드
'''
    [사고과정]
    적절하게 자료 구조 사용하면 해결될 문제일 듯
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memopad = set()
res = [] # 결과를 저장하는 배열
for _ in range(n): # 메모장에 있는 키워드 입력받기
    memopad.add(input().rstrip())

for _ in range(m): # 쉼표(,)로 구분되어 있는 키워드 개수 알아보기 --> O(2*10^5*10)
    keywords = input().strip().split(',')
    for keyword in keywords: # ---> O(10)
        memopad.discard(keyword) # 'discard' 사용하면, 요소가 없어도 에러가 안 남.
    res.append(len(memopad))

# 결과 출력
for e in res:
    print(e)