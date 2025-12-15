# 문자열 교환
'''
    b를 연속으로 만드는 최소 이동 횟수.. 등등
    뭐 여러가지 생각해 봤는데, 떠오르는 게 없어서..
    힌트 다시 봄 --> 슬라이딩 윈도우?
    아 ㅁㅊ / 어차피 문자열 길이 최대 1000밖에 안되니까 브루트포스 하는구나..
'''
s = input()
a_cnt = 0 # a의 개수
for e in s:
    if e == 'a':
        a_cnt += 1

# 슬라이딩 윈도우로 풀어봐라
# ---> 슬라이딩 윈도우의 크기는 a의 갯수만큼, 그 안에 b 있으면 교환해야 하니까...
test = s + s
min_val = int(1e9)
for i in range(len(s)):
    window = test[i:i+a_cnt]
    cnt = 0
    for e in window:
        if e == 'b':
            cnt += 1
    min_val = min(cnt, min_val)

print(min_val) # 정답 출력