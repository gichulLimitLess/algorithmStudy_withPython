# A와 B
'''
    [사고과정]
    연산을 할 때, 이거 뭔가.. 현재 한 액션이 이후에 영향을 미치지 않는 것 같은 '냄새'를 맡았다
    --> '그리디'를 써야 할 것 같다 (각 사건이 독립이라는 걸 캐치함)
'''
s = input()
t = input()

# # 아래 프로세스 ---> 최악의 경우 O(10만) / 충분히 가능할 듯
# def making(s, t):
#     visited = set()
#     while True:
#         if s == t: # 만들 수 있게 되었다면
#             return 1
#         elif len(s) == len(t): # 길이가 같아졌는데, 서로 다른 내용이라면 --> 더 이상 같게 만들 방법 없음
#             return 0
#         else:
#             # 1. 문자열 뒤에 A 추가
#             imsi = s + 'A'
#             print(imsi)
#             if imsi == t[:len(imsi)]:
#                 s = imsi
#                 continue
#
#             # 2. 문자열 뒤집고 뒤에 B 추가
#             imsi = 'B' + s
#             imsi_rev = imsi[::-1]
#             print(imsi_rev)
#             if imsi_rev == imsi_rev[:len(imsi_rev)]:
#                 s = imsi_rev
#                 continue
#
# print(making(s, t))

'''
    [오답노트]
    --> 정방향으로 못 풀겠으면.. 역방향으로 한 번 생각해보자!!
'''