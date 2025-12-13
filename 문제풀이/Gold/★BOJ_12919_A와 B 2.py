# A와 B 2
'''
    [사고과정]
    다시 떠올려야 한다 --> 정방향으로 갈 경우, 2^50 모두 고려 / 시간 매우 터짐
    그럴 경우 어떻게 해야 한다? --> "역방향"으로 가봐라
    -------------------------------------------
    T로부터 S로 가본다
        -> T의 맨 뒤가 A다:
            근데 사실, A를 짜르는 것만으로도 해결되지 않나? B 만났을 때만 처리해보면 되지 않을까..
        -> T의 맨 뒤가 B다: B가 여기 올 수 있는 경우는 B가 맨 앞에 있을 때 뒤집는 방법 뿐
'''
S = input().strip()
T = input().strip()

found = False

def dfs(t):
    global found
    if found:
        return
    if len(t) < len(S):
        return
    if t == S:
        found = True
        return

    # 규칙 1: 뒤가 A면 제거
    if t[-1] == 'A':
        dfs(t[:-1])

    # 규칙 2: 앞이 B면 제거 + 뒤집기
    if t[0] == 'B':
        dfs(t[1:][::-1])

dfs(T)
print(1 if found else 0)

