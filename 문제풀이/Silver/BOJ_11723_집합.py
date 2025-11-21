# 집합
import sys
input = sys.stdin.readline
write = sys.stdout.write

m = int(input())
S = 0   # 비트마스크

for _ in range(m):
    instr = input().split()
    cmd = instr[0]

    if cmd == "add":
        S |= (1 << (int(instr[1]) - 1))

    elif cmd == "remove":
        S &= ~(1 << (int(instr[1]) - 1))

    elif cmd == "check":
        write('1\n' if S & (1 << (int(instr[1]) - 1)) else '0\n')

    elif cmd == "toggle":
        S ^= (1 << (int(instr[1]) - 1))

    elif cmd == "all":
        S = (1 << 20) - 1

    elif cmd == "empty":
        S = 0


