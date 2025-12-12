# 경로 찾기
'''
    [사고과정]
    플로이드-워셜의 쉬운 버전으로 풀면 되지 않을까?
'''
n = int(input()) # 정점의 개수 n (1 <= n <= 100)

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# 플로이드 워셜 수행 --> i를 출발해 k를 거쳐 j로 가는게 효율적일 경우 해당 값을 갱신
# --> 그러한 큰 틀을 이용해서, 거쳐가는 경로가 있을 경우 1을 넣도록 한다
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

# dist를 출력하면, 그거 자체가 나옴
for row in graph:
    for e in row:
        print(e, end=' ')
    print()
