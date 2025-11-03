# 거짓말
'''
    [풀이과정]
    - 처음엔 이것을 '그래프' 문제라고 인지하고 들어왔다.'
    - 그러나, 이것은 '그래프'로 푸는 것보다, 'set' 자료형으로 푸는게 훨씬 효율적이라는 것을 깨달았다.
    ---> 결국 구해야 할 것은, "진실을 알고 있는 사람들" + "진실을 알고 있는 사람들과 같이 파티에 있던 사람들"
         이외의 사람들 앞에선 과장되게 얘기해도 상관 없다.
'''

# # 사람 수 n, 파티 수 m (0 <= n, m <= 50)
# n, m = map(int, input().split())
# cannot_lying = set()
#
# # 1. 진실을 알고 있는 사람들 일단 set에 넣기
# input_list = list(map(int, input().split()))
# for e in input_list[1:]:
#     cannot_lying.add(e)
#
# parties = []
# for _ in range(m):
#     row = list(map(int, input().split()))[1:]
#     parties.append(row)
#
# # 2. 입력을 뒤져 보면서, 진실을 알고 있는 사람들과 "같이 있던" 사람들 탐색
# for party in parties: # ----> O(50 * (50 + 50))
#     isWith = False
#     imsi = []
#     for person in party: # ---> O(50)
#         if person in cannot_lying: # 진실을 알고 있던 사람이랑 같이 있었다면
#             isWith = True
#         imsi.append(person)
#
#     if isWith: # 같이 있었다면
#         for e in imsi: # 임시로 넣어놨던 멤버들 다 "진실만 말해야 하는 사람들"에 집어 넣기 ---> O(50)
#             cannot_lying.add(e)
#
# # 3. 다시 parties 탐색 하면서, 과장된 얘기 해도 되는 곳 체킹
# cnt = 0
# for party in parties: # ----> O(50 * 50)
#     check = 0 # 몇 명을 지나쳤는지 확인
#     for person in party:
#         if person in cannot_lying: # "진실만 말해야 하는 사람들"에 포함된 애가 발견되었다면
#             break
#         check+=1
#     if check == len(party): # party의 length만큼 정확히 세졌다면
#         cnt += 1
#
# print(cnt) # 정답 출력

'''
    아래가 정답 코드
'''

# 거짓말 (BOJ 1043)
# https://www.acmicpc.net/problem/1043

def find(x):
    # 경로 압축(Path Compression)
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    # 서로 다른 집합이면 합친다
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a  # b 루트를 a 루트에 연결


# 1. 입력
n, m = map(int, input().split())
truth_info = list(map(int, input().split()))
truth_known = truth_info[1:]  # 첫 번째 원소는 진실 아는 사람 수
parties = [list(map(int, input().split()))[1:] for _ in range(m)]

# 2. 초기화
parent = [i for i in range(n + 1)]  # 1-based 인덱스

# 3. 같은 파티에 있는 사람들은 모두 연결(Union)
for party in parties:
    for i in range(1, len(party)):
        union(party[0], party[i])

# 4. 진실 아는 사람들의 루트 집합 계산
truth_roots = {find(x) for x in truth_known}

# 5. 각 파티별로 판별
cnt = 0
for party in parties:
    # 파티의 모든 참가자가 truth_roots에 포함되지 않으면 거짓말 가능
    if all(find(p) not in truth_roots for p in party):
        cnt += 1

print(cnt)

