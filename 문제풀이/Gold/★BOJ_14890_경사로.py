# 경사로
'''
    [사고과정]
    문제를 읽고 나서 생각해보니.. 이것은 '브루트포스'로 충분히 해결할 수 있을 것 같은 문제
    --> 효율적으로 '경사로 설치' 여부 판별을 위해서 '스택'을 사용해도 좋을 것 같단 생각이 들었음
'''
# import copy
#
# n, l = map(int, input().split())
# board = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     board.append(row)
#
# cnt = 0
# # board의 행 기준으로 한 줄씩 먼저 살펴보기
# for i in range(n):
#     row = copy.deepcopy(board[i])
#     stack = []
#     s = 0
#     for j in range(n):
#         # 처음에 비어있는 경우
#         if len(stack) == 0:
#             stack.append(row[j])
#         # 앞에 넣었던 것들이 지금 넣으려는 것과 '1' 차이나는 경우
#         elif len(stack)-s >= l and abs(row[j]-stack[-1]) == 1:
#             stack.append(row[j])
#             s = len(stack)-1
#         elif len(stack)-s < l or abs(row[j]-stack[-1]) > 1: # 이 경우에는 더 이상 검사하면 안됨
#             break
#         else: # 이 경우는 그냥 같은 경우임
#             stack.append(row[j])
#
#     if len(stack) == n:
#         cnt += 1
#         continue
#
#     stack = []
#     for j in range(n-1, -1, -1):
#         # 처음에 비어있는 경우
#         if len(stack) == 0:
#             stack.append(row[j])
#         # 앞에 넣었던 것들이 지금 넣으려는 것과 '1' 차이나는 경우
#         elif len(stack) - s >= l and abs(row[j] - stack[-1]) == 1:
#             stack.append(row[j])
#             s = len(stack) - 1
#         elif len(stack) - s < l or abs(row[j] - stack[-1]) > 1:  # 이 경우에는 더 이상 검사하면 안됨
#             break
#         else:  # 이 경우는 그냥 같은 경우임
#             stack.append(row[j])
#
#     if len(stack) == n:
#         cnt += 1
#         continue
#
# # board의 열 기준으로 한 줄씩 또 살펴보기
# for i in range(n):
#     col = [board[j][i] for j in range(n)]
#     stack = []
#     s = 0
#     for j in range(n):
#         # 처음에 비어있는 경우
#         if len(stack) == 0:
#             stack.append(col[j])
#         # 앞에 넣었던 것들이 지금 넣으려는 것과 '1' 차이나는 경우
#         elif len(stack)-s >= l and abs(col[j]-stack[-1]) == 1:
#             stack.append(col[j])
#             s = len(stack)-1
#         elif len(stack) - s < l or abs(col[j] - stack[-1]) > 1:  # 이 경우에는 더 이상 검사하면 안됨
#             break
#         else:  # 이 경우는 그냥 같은 경우임
#             stack.append(col[j])
#
#     if len(stack) == n:
#         cnt += 1
#         continue
#
#     stack = []
#     for j in range(n-1, -1, -1):
#         # 처음에 비어있는 경우
#         if len(stack) == 0:
#             stack.append(col[j])
#         # 앞에 넣었던 것들이 지금 넣으려는 것과 '1' 차이나는 경우
#         elif len(stack) - s >= l and abs(col[j] - stack[-1]) == 1:
#             stack.append(col[j])
#             s = len(stack) - 1
#         elif len(stack) - s < l or abs(col[j] - stack[-1]) > 1:  # 이 경우에는 더 이상 검사하면 안됨
#             break
#         else:  # 이 경우는 그냥 같은 경우임
#             stack.append(col[j])
#
#     if len(stack) == n:
#         cnt += 1
#         continue
#
# print(cnt)

'''
    (오답노트)
    -> 위 문제는 추상화하는 순간 틀린다.
        --> 조건을 그대로 받아 적고, 상태 배열로 관리하는 절차 지향 사고를 체화하자
    [아래는 정답 코드]
'''
import sys
N, L = map(int,sys.stdin.readline().split())
pan = []
for i in range(N):
    pan.append(list(map(int,sys.stdin.readline().split())))

answer = 0

# 경사로를 놓을 수 없는 경우
# 경사로를 놓은 곳에 또 경사로를 놓는 경우
# 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우 O
# 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
# 경사로를 놓다가 범위를 벗어나는 경우
def if_can_line(line):
    bri = [False for _ in range(N)]
    for i in range(1, N):
        # 줄에서 높이차이가 1보다 크다면 경사로를 못 두기때문에 return False
        if abs(line[i - 1] - line[i]) > 1:
            return False
        else:
            if (line[i - 1] - line[i]) == 1:  # 오른쪽으로 다리 놓을 때
                for j in range(L):  # 놓을 수 있는지 확인하기 위해 경사로 길이만큼 반복
                    if i + j >= N:  # 경사로가 범위 밖으로 나간다면
                        return False
                    if line[i] != line[i + j]:  # 경사로를 두는 곳의 높이가 다르면
                        return False
                    if bri[i + j] == True:  # 경사로가 이미 있다면
                        return False
                    if bri[i + j] == False:  # 경사로를 두는데 문제가 없다면
                        bri[i + j] = True

            elif (line[i - 1] - line[i]) == -1:  # 왼쪽으로 다리 놓을 떄
                for j in range(L):
                    if i - 1 - j < 0:
                        return False
                    if line[i - 1] != line[i - 1 - j]:
                        return False
                    if bri[i - 1 - j] == True:
                        return False
                    if bri[i - j - 1] == False:
                        bri[i - j - 1] = True
    return True  # 경사로를 놓는데에 아무런 문제가 없다면

for i in range(N):
    if if_can_line(pan[i]):
        answer+=1
for j in range(N):
    if if_can_line([pan[i][j] for i in range(N)]):
        answer+=1

print(answer)