# 비슷한 단어
'''
    [사고과정]
    - '접두사'의 길이가 최대인 경우, 그 두 단어를 출력
    - '접두사'의 길이가 최대인 경우가 여러 경우가 있을 때는, 그냥 순서대로 맨 앞에 2개 출력
        --> '입력된 순서'대로 출력되어야 하고, N이 최대 2만이므로, O(N^2)인 풀이는 위험하다
        --> O(N)으로 줄이는 방법 없을까?
    - 문자열의 최대 길이가 100 / DP의 편집 거리를 쓰는 문제는 아닌 것 같음
        --> 애초에, 쌍을 찾아내는 문제기 때문에 그거와 연관 없다고 생각했음
        --> 그러면, 무엇을 풀어야 하는가? 길이를 하나씩 늘려가 보면서, 해당 부분 문자열에 겹치는 게 없으면 삭제해도 되지 않을까?
    - 근데, 문자열을 저장하는 것보다.. 해당 문자열의 '인덱스'를 저장하는 게 효율적일 것 같다.
        --> 결국, 결과가 여러 개면 입력된 순서대로 앞에 2개만 출력해야 하니깐!
'''
# n = int(input()) # 단어 개수 n
# vocab_list = []
# disable = [False for _ in range(n)] # 더 이상 확인할 단어가 아닌 것을 표시
# for _ in range(n):
#     vocab_list.append(input())
#
# v_len = 1 # 접두사 첫 길이는 1로 시작
# while True: # 최대 100번 반복할 것임 --> O(100 * 6만)
#     check_dict = dict() # key: '접두사' / value: 해당 단어들의 vocab_list에서의 "인덱스"
#     # 1. 단어 하나씩 보기 --> O(2만)
#     for idx, vocab in enumerate(vocab_list):
#         if not disable[idx]: # disable 된 경우가 아닐 때만 고려 해야 한다
#             prefix = vocab[:v_len] if len(vocab) >= v_len else vocab
#             if prefix in check_dict: # 접두사가 같은 게 있다면
#                 check_dict[prefix].append(idx)
#             else:
#                 check_dict[prefix] = [idx]
#
#     # 2. 짝을 이루지 못하는 게 있다면, 삭제를 고려해 봐야 한다 --> O(2만)
#     isEnd = True
#     candidate = []
#     for check in check_dict.values(): # 들어온 배열의 '길이'를 보고 혼자만 있는 경우 판단
#         if len(check) == 1: # 2개 이상 같은 경우가 없다면
#             candidate.append(check[0])
#         else: # 2개 이상인 경우가 하나라도 있다면, 끝내면 안된다
#             isEnd = False
#
#     # 3. 2개 이상인 경우가 하나도 나오지 않았다면, 현재 삭제할 후보군들(candidate)들이 결국 정답 후보들이다 --> O(2만)
#     #     --> 그 중에서, 인덱스 값이 제일 작은 두 놈을 골라서 답을 출력하면 끝이다
#     if isEnd:
#         candidate.sort()
#         print(vocab_list[candidate[0]])
#         print(vocab_list[candidate[1]])
#         break
#     else: # 하나라도 나왔다면, 삭제 후보들을 disable 시켜 준다
#         for e in candidate:
#             disable[e] = True
#         v_len += 1 # 비교하는 길이 +1

# ================ 아래가 정답 코드 ==================
n = int(input())
a = [input() for _ in range(n)]

# n = 9
# a = ["noon", "is", "for","lunch","most","noone","waits","until","two"]

# 입력받은 문자들을 인덱스와 함께 사전순으로 정렬한다.
b = sorted(list(enumerate(a)), key=lambda x: x[1])


# b = [(2, 'for'), (1, 'is'), (3, 'lunch'), (4, 'most'), (0, 'noon'), (5, 'noone'), (8, 'two'), (7, 'until'), (6, 'waits')]

# check 함수는 글자 하나하나가 서로 같은지 탐색
def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            cnt += 1
        else:
            break
    return cnt


# 최장 접두사를 가진 문자열 담아둘 리스트 생성
length = [0] * (n + 1)
maxlength = 0

for i in range(n - 1):
    # 인접한 두개의 문자열을  check함수에 대입
    # tmp 값은 동일한 접두사의 길이
    tmp = check(b[i][1], b[i + 1][1])
    # 최장 접두사 길이 갱신
    maxlength = max(maxlength, tmp)

    # b[i][0]은 문자가 입력된 순서, 즉 인덱스
    # length 에 입력된 순서에 자기 접두사 길이를 저장
    # max 함수로 이전 값하고 현재 값하고 비교하여 집어넣음
    length[b[i][0]] = max(length[b[i][0]], tmp)
    length[b[i + 1][0]] = max(length[b[i + 1][0]], tmp)
    # length = [4, 0, 0, 0, 0, 4, 0, 0, 0, 0]

first = 0
for i in range(n):
    # 입력된 순서대로 접두사의 길이 비교
    if first == 0:
        # 만약 현재 접두사의 길이가 최장접두사라면
        if length[i] == max(length):
            # 제일 먼저 입력된 문자 출력
            first = a[i]
            print(first)
            pre = a[i][:maxlength]
    else:
        # 다음으로 입력되었된 값들 중 최장 접두사 출력후 종료
        if length[i] == max(length) and a[i][:maxlength] == pre:
            print(a[i])
            break