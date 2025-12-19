# 햄버거 분배
'''
    [사고과정]
    각 칸마다, 그 칸을 중심으로 모든 칸 완전탐색 해도 시간 초과 안됨 --> O(2만 * 20)
    그대로 가보자 / 아 참고로, 자기 기준으로 가장 '왼쪽'부터 보면 될 듯 ('미래 선택지'를 보존하는 쪽이 항상 안전하다)
'''
n, k = map(int, input().split())
table = input()
visited = [False for _ in range(n)]
max_cnt = 0
# 테이블 순회 ---> O(20000 * 20)
for idx, e in enumerate(table):
    if e == 'P': # 사람이 경우, 이를 기준으로 +-k 범위 내에서 먹을 수 있는 햄버거 있는지 '먼 곳'부터 검사
        start = idx-k if idx-k >= 0 else 0
        end = idx+k if idx+k <= n-1 else n-1
        # 왼쪽 & 오른쪽 검사 ---> O(20)
        for i in range(start, end+1):
            if i == idx: # 자기 자신은 방문 처리만 하고 패스
                visited[i] = True
                continue
            if not visited[i] and table[i] != 'P': # 방문한 곳이 아니고(먹지 않았고), 사람이 아닌 칸이면
                visited[i] = True # 방문 표시
                max_cnt += 1
                break # 바로 빠져 나온다

print(max_cnt) # 이게 바로 '햄버거를 먹을 수 있는 사람의 최대 수'