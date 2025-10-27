# 스도쿠
'''
    [오답노트]
    -> 백트래킹은.. 재귀로 들어갔다가 원상복귀 때리는 형식(sudoku[y][x]=0)으로도 간단히 구현 가능!
        무조건... deepcopy를 해야 한다는 강박이 내 발목을 또 붙잡았다.
    -> "유효하지 않으면 바로 return" 이라는 가지치기 설계로 해결 가능한 것을 알아 챘으나..
        그렇게 해도 될까? 라는 공포심 때문에 해결하는 데 애를 먹는다.
    -> 이러한 단순하지 않은 "구현" 문제는.. 테스트 가능한 단위로 쌓아가면서 문제를 풀어야 한다
        ex)
        1. 입력 -> 2. 빈칸 좌표 수집 -> 3. 한 칸 채우는 함수 구현 -> 4. 유효성 검사 함수 -> 5. DFS 백트래킹 연결
    -> "틀리면 어쩌지?" 이러지 말고, "틀려도 좋으니, 한 칸만 먼저 채워보자" 마인드로 가자
        완벽히 머릿속으로 검증하려 하지 말고, 일단 print로 경로 찍으면서 눈으로 확인해라
'''

sudoku = []
for _ in range(9):
    row = list(map(int, input()))
    sudoku.append(row)
blank = []

def row(a, n): # 가로
    for i in range(9):
        if n == sudoku[a][i]: # 이미 있으면
            return False
    return True

def column(a, n): # 세로
    for i in range(9):
        if n == sudoku[i][a]: # 이미 있으면
            return False
    return True

def square(y, x, n): # 3x3 칸
    for i in range(3):
        for j in range(3):
            if n == sudoku[y//3 * 3 + i][x//3 * 3 + j]: # 칸내에 이미 있으면
                return False
    return True

def find(n):
    if n == len(blank): # 빈 공간 만큼 사용했으면
        for i in sudoku: # 출력 후
            for e in i:
                print(e, end='')
            print() # 한 칸 띄우기 (개행)
        exit() # 강제 종료

    for i in range(1,10):
        y = blank[n][0]
        x = blank[n][1]
        if column(x,i) and row(y,i) and square(y, x, i):
            sudoku[y][x] = i
            find(n+1)
            sudoku[y][x] = 0

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])

find(0)