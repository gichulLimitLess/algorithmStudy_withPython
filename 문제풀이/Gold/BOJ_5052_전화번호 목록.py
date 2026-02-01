# 전화번호 목록
'''
    tc 개수 최대 50개
    전번 개수 최대 1만개
    전번 길이는 최대 10자리
'''

def check():
    n = int(input())
    tel_num_list = []
    # 전번 개수 n개 만큼 입력 받기 --> O(1만)
    for _ in range(n):
        input_val = input()
        tel_num_list.append(input_val)
    # 전번 개수 n개만큼 정렬 --> O(1만 * log1만)
    tel_num_list.sort()
    # 전번 list에서 앞뒤로 확인 --> O(10*2*1만)
    for i in range(len(tel_num_list) - 1):
        # 앞에 친구가 뒤의 놈의 일부의 접두어인 경우
        if tel_num_list[i] == tel_num_list[i + 1][:len(tel_num_list[i])]:
            return 'NO'
    # 중간에 'NO' 안 거치고 여기까지 잘 왔음 --> 일관성 있는 경우, 즉 'YES' 반환
    return 'YES'

tc = int(input())
# 총 시간 복잡도: O(50 * (1만 + 14만 + 20만)) --> O(2천만) 밑이라 1초 안에 통과 쌉가능일듯
for _ in range(tc):
    print(check())