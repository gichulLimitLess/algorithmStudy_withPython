# 디지털 티비
def main():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    channels = [input().strip() for _ in range(n)]

    # find indices
    idx1 = channels.index("KBS1")
    idx2 = channels.index("KBS2")

    result = []

    # move KBS1 to the top
    result.append("1" * idx1)  # move cursor down to KBS1
    result.append("4" * idx1)  # bring KBS1 up to position 0

    # if KBS1 was below KBS2 originally, moving it up shifts idx2 down by 1
    if idx1 > idx2:
        idx2 += 1

    # move KBS2 to second position
    result.append("1" * idx2)       # move cursor down to KBS2
    result.append("4" * (idx2 - 1)) # bring KBS2 up to position 1

    print("".join(result))

if __name__ == "__main__":
    main()
