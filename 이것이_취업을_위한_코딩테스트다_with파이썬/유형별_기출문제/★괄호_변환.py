def is_correct(p):
    stack = []
    for ch in p:
        if ch == '(':
            stack.append(ch)
        else:  # ')'
            if not stack:
                return False
            stack.pop()
    return not stack


def reverse(u):
    return ''.join('(' if ch == ')' else ')' for ch in u)


def solution(p):
    # 1. 빈 문자열이면 반환
    if not p:
        return ""

    # 2. u, v 분리 (u = 최소 균형잡힌 문자열)
    balance = 0
    for i in range(len(p)):
        if p[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:  # 균형 잡혔을 때
            u, v = p[:i+1], p[i+1:]
            break

    # 3. u가 올바른 문자열이면
    if is_correct(u):
        return u + solution(v)
    else:
        # 4. 아니라면
        return "(" + solution(v) + ")" + reverse(u[1:-1])


# ======= 오답 노트 =======
# -> 소스코드를 최대한 단순화 하려면... 함수화를 잘 해야 한다!!!