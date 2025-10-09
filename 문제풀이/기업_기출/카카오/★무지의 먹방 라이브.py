# 무지의 먹방 라이브
# 이 코드는 프로그래머스에서 돌아가는 거라, 거기서 돌려야 정상 동작함!
import heapq  # 우선순위 큐에 넣게 되면, 없는 음식은 알아서 빠지게 됨


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        print(-1)

    # 시간이 작은 음식부터 빼야하니까, 우선순위 큐 사용하자
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수 (처음엔 food_times의 length)

    # "sum_value + (현재의 음식 시간 - 이전의 음식 시간) * 현재 음식 개수"와 k 비교
    # q의 맨 앞에 꺼가 "우선순위가 가장 높은 것"
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]  # 맨 위에꺼 일단 빼고
        sum_value += (now - previous) * length  # 이게 결국 걸린 시간만큼 sum_value 해주는 거임
        length -= 1  # 다 먹은 음식 제외
        previous = now  # 이전에 먹은 음식 갱신 (이걸로, 다음 꺼 갱신해서 써야함)

    # 남은 음식 중에서 몇 번째 음식인지 확인해 출력
    result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준 정렬
    return result[(k - sum_value) % length][1]