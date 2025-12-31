# 덩치
'''
    어쩔 수 없이 O(N^2)으로 풀어야 할 것 같음
    --> 그러나, N이 50이기 때문에 충분히 그렇게 풀어도 됨
'''
n = int(input())
people = []

for _ in range(n):
    x, y = map(int, input().split())
    people.append((x, y))

for i in range(n):
    rank = 1
    for j in range(n):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    print(rank, end=' ')
