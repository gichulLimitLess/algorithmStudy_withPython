from collections import deque  # 큐 사용을 위함

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    # 초기 덧셈 값 저장, target값 지정 및 초기 길이 합 저장
    sum1 = sum(q1)
    sum2 = sum(q2)
    target = (sum1 + sum2) // 2
    if (sum1 + sum2) % 2 != 0:  # 나머지가 있으면, 절대 같아질 수 없다
        return -1

    first_len = len(q1) * 3  # 초기 길이 합 --> 이건.. 그냥 직관적으로 이해하자
    answer = 0

    while sum1 != target or sum2 != target:  # 둘 다 target일 때만 while문 탈출
        if answer == first_len:  # 카운트가 길이 합이랑 같은 경우 == 처음으로 다시 빽도한 경우
            return -1

        # q1 기준으로만 보면 된다 (-> 알아서 q2의 입장에서도 보게 되는 거다)
        if sum1 > target:  # sum1의 값이 target값보다 크다 -> q1에서 하나 빼야 한다
            temp = q1.popleft()
            sum1 -= temp
            q2.append(temp)
            sum2 += temp
            answer += 1  # 연산 횟수 1회 증가
        elif sum1 < target:  # sum2의 값이 target값보다 작다 -> q1에 하나 넣어줘야 한다
            temp = q2.popleft()
            sum2 -= temp
            q1.append(temp)
            sum1 += temp
            answer += 1  # 연산 횟수 1회 증가

    return answer  # answer 자체가 최소 연산 횟수 (여기 빠져 나왔으면, 최소 횟수로 한거임)