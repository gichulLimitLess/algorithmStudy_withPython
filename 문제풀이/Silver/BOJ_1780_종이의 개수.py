# 종이의 개수
'''
    분할 정복 문제는 대부분.. 재귀 함수를 쓰는 것 같은데..
    --> 재귀 함수를 쓸 때의 두려움을 극복해야 한다
'''
n = int(input())
board = []
for _ in range(n):
    row = list(map(int, input().split(' ')))
    board.append(row)

# 순서대로 -1, 0, 1로 이루어진 종이 개수
cnt_of_m1 = 0
cnt_of_zero = 0
cnt_of_1 = 0

# 찾기
def find(s_y, s_x, size):
    global cnt_of_m1, cnt_of_zero, cnt_of_1
    check_set = set()
    for i in range(s_y, s_y+size):
        for j in range(s_x, s_x+size):
            check_set.add(board[i][j])

    if len(check_set) > 1: # 모두 같은 원소로 이루어져 있지 않다면
        for i in range(s_y, s_y+size, size//3):
            for j in range(s_x, s_x+size, size//3):
                find(i, j, size//3)
    else: # 종이의 모든 내용이 같다면, 그에 따라서 해당하는 개수 출력
        if -1 in check_set:
            cnt_of_m1 += 1
        elif 0 in check_set:
            cnt_of_zero += 1
        elif 1 in check_set:
            cnt_of_1 += 1
# 찾기
find(0, 0, n)

# 결과 출력
print(cnt_of_m1)
print(cnt_of_zero)
print(cnt_of_1)