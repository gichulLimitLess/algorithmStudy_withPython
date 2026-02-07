import sys

def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())

    # 항상 작은 수 n1, 큰 수 n2
    n1, n2 = min(A, B), max(A, B)

    # 사이 정수 개수
    count = max(n2 - n1 - 1, 0)
    print(count)

    # 사이 정수가 있으면 출력
    if count > 0:
        nums = range(n1 + 1, n2)
        print(*nums)


if __name__ == "__main__":
    main()
