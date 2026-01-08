# 비밀번호 발음하기
while True:
    password = input().strip()
    # 종료 조건
    if password == "end":
        break

    vowels = set("aeiou")
    has_vowel = False

    acceptable = True

    # 연속된 모음/자음 개수
    vowel_count = 0
    consonant_count = 0

    prev_char = ""  # 이전 문자

    for char in password:
        # 모음 확인
        if char in vowels:
            has_vowel = True
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0

        # 모음/자음 3개 연속 체크
        if vowel_count == 3 or consonant_count == 3:
            acceptable = False
            break

        # 같은 글자 2번 연속 체크 (단 "ee", "oo"는 허용)
        if prev_char == char:
            if not (char == 'e' or char == 'o'):
                acceptable = False
                break

        prev_char = char

    # 모음이 하나도 없는 경우
    if not has_vowel:
        acceptable = False

    # 출력
    if acceptable:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")

