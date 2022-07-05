"""
문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
"""

def solution(s):

    answer = ''
    i = 0
    for ch in s:
        if ch == ' ':
            answer += ch
            i = 0
        else:
            if i % 2 == 0:
                answer += ch.upper()
            else:
                answer += ch.lower()
            i += 1
    return answer
# def solution(s):
#     # answer = []
#     answer = ''
    
#     for i in range(len(s)):
#         if i % 2 != 0:
#             answer += s[i].lower()
#             # answer.append(s[i].lower())
#         elif i % 2 == 0:
#             answer += s[i].upper()
#             # answer.append(s[i].upper())
#         elif s[i] == '':
#             # answer.append('')
#             answer += ''
#     # b = ''.join(answer)
#     return answer
# def solution(s):
#     answer = ''
#     a = []
#     for i in range(len(s)): 
#         a = s.split(" ")
#     print(a[0])
    
#     return answer