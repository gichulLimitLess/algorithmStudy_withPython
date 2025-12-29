# 접미사 배열
'''
    문자열 S가 주어졌을 때, 우선 모든 접미사를 구하는 게 목표임
    그리고, 그것에 대해서 sort() 때려주면 끝남
'''
vocab = input()
tail_list = [] # 접미사 모아놓은 곳
for i in range(len(vocab)): # --> O(1000^2)
    tail_list.append(vocab[i:len(vocab)])
tail_list.sort() # 사전순으로 정렬 ---> O(100만 * log100만)

# 결과 출력 --> O(1000^2)
for tail in tail_list:
    print(tail)