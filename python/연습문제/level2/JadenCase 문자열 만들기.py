"""
문제 설명
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
"""

# import string

# def solution(s):
#     return ' '.join(map(lambda s: s[0].upper() + s[1:].lower() if s else s, s.split(' ')))

import re
def solution(s):
    temp=[]
    # s=s.lower()
    # s=s.replace(s[0],s[0].upper())
    s = s.capitalize()
    
    #공백1개이상 + 문자1개로 된거 찾기
    temp=re.findall(' +\w', s)
    #print(temp)

    for i in temp:
        s=s.replace(i,i.upper())
    return s



    # return " ".join([i.title() for i in s.split(' ')])
#     answer = ''
#     # a = []
#     # a = s.split(" ")
    
#     s = s.split(' ')
#     for i in s:
#         answer += i.capitalize()
#         answer += " "
    
#     # answer= string.capwords(s)
#     # print("The capitalized string is:", cap_strng)
    
#     answer = answer.rstrip()
#     # answer = answer.lstip()
#     # print(a)
#     return answer