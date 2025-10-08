# 단어 정렬
# 1. 길이가 짧은 것부터 / 2. 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 함 -> set 사용해서 중복 제거 / 그런 다음 다시 list로 만들어야 할 듯

n = int(input()) # 단어 갯수 n
vocab_list = []
for _ in range(n):
    vocab = input()
    vocab_list.append(vocab)

vocab_list = list(set(vocab_list)) # set으로 변환했다가, 다시 list로 가는거 -> 중복 제거하는 좋은 테크닉?
vocab_list.sort(key=lambda x: (len(x), x)) # 길이가 짧은 것부터, 길이가 같으면 사전 순으로

for vocab in vocab_list:
    print(vocab)