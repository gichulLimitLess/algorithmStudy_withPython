# LCS
# 문자열의 크기가 최대 1000, 그런데, 그거를 일일이 조합으로 보려면 개에바임
# --> DP로 bottom-up 때려갖고 해결하자!

s1 = list(input())
s2 = list(input())

lcs = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]: # 현재 비교하는 것이 같다면
            lcs[i][j] = lcs[i-1][j-1] + 1 # LCS 길이 + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(max(map(max, lcs))) # lcs 배열에서, 최댓값을 뽑아낸다