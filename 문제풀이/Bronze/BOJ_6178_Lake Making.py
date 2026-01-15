# Lake Making
import sys

input = sys.stdin.readline

R, C, E, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

for _ in range(N):
    r, c, d = map(int, input().split())
    # 1-based -> 0-based
    r -= 1
    c -= 1

    # find max in 3x3
    max_h = 0
    for i in range(r, r+3):
        for j in range(c, c+3):
            if grid[i][j] > max_h:
                max_h = grid[i][j]

    target = max_h - d
    # lower elements above target
    for i in range(r, r+3):
        for j in range(c, c+3):
            if grid[i][j] > target:
                grid[i][j] = target

total_depth = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] < E:
            total_depth += (E - grid[i][j])

# multiply by area 6ftx6ft = 72in x 72in
print(total_depth * 72 * 72)
