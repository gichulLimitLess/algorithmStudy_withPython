# 요세푸스 문제 0
'''
    가볍게 1을 기준으로 K-1씩 올리면서 진행한다
'''
n, k = map(int, input().split())
now = 0
num_list = [i+1 for i in range(n)]
res = []

# num_list가 길이가 0이 될 때까지 반복 --> O(1000 * 1000)
while len(num_list) > 0:
    now = (now + (k-1)) % (len(num_list)) # 원형이므로 이런식으로 돌아가야 한다
    res.append(str(num_list[now])) # 결과에 담기
    del num_list[now] # 없앤다

print('<' + ', '.join(res) + '>')