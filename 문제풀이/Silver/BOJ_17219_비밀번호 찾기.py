# 비밀번호 찾기
'''
    자동으로 dict와 sys.stdin.readline 생각나는 문제
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
info_dict = dict()

# 1. 사이트별 비밀번호 입력받기
for _ in range(n):
    addr, pw = input().split()
    info_dict[addr] = pw # dict의 key로 사이트 주소, value로 비밀번호 저장

# 2. 비밀번호 찾기
for _ in range(m):
    addr = input().rstrip()
    print(info_dict[addr]) # info_dict에 저장되어 있는 해당 정보 출력