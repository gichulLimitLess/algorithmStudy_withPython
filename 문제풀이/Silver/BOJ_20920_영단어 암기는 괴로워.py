# 영단어 암기는 괴로워
'''
    우선순위 정보
    1. 자주 나오는 단어일수록 앞에 배치
    2. 해당 단어의 길이가 길수록 앞에 배치
    3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
    --> 길이가 M 이상인 단어만 외우도록 함
'''
import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
vocabs = []
for _ in range(n):
    vocab = input().rstrip()
    if len(vocab) >= m: # 길이가 m 이상인 단어들만 외우기
        vocabs.append(vocab)

vocabs_counter = dict(Counter(vocabs)) # 각 단어 등장 횟수
# 자주 나오는 단어일수록 앞에 정렬, 단어 길이가 길수록 앞에 배치, 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
vocab_list = []
for vocab, count in vocabs_counter.items():
    vocab_list.append((count, len(vocab), vocab))

vocab_list.sort(key=lambda x: [-x[0], -x[1], x[2]])
# 결과 출력
for vocab in vocab_list:
    print(vocab[2])