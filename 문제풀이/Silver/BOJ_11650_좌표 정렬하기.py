# 좌표 정렬하기
'''
    2차원 좌표를 정렬해 보는 매우 간단한 문제
    -> Python에서는 sort() 사용할 경우.. 튜플의 첫번째 원소부터 기준으로 알아서 잘 정렬해준다
    -> n의 최대는 10만 --> 시간 복잡도는.. O(10만*log10만)
'''
import sys
input = sys.stdin.readline

dots = []
n = int(input())
for _ in range(n):
    xi, yi = map(int, input().split())
    dots.append((xi, yi))

dots.sort() # 오름차순 정렬
for dot in dots:
    print(dot[0], dot[1])