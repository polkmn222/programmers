"""
문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
"""
def solution(s, n):
    answer = ''
    a = []
    for i in range(len(s)):
        b = 0
        c = 0
        if s[i] == ' ':
            answer += ' '
        elif 97 <= ord(s[i]) <= 122:
            c = ord(s[i]) + n
            if c > ord('z'):
                c -= 26
            answer += chr(c)
        elif 65 <= ord(s[i]) <= 90:
            b = ord(s[i]) + n
            if b > ord('Z'):
                b -= 26
            answer += chr(b)
        # else:
        # elif 97 <= ord(s[i]) <= 122:
        #     c = ord(s[i]) + n
        #     if c > ord('Z'):
        #         c -= 26
        #     answer += chr(c)
    return answer
