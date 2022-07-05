"""
문제 설명
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.
"""

# def solution(s):
#     answer = True
#     for i in range(len(s)):
#         if s[i] == "a" and s[i + 1] == "2" and s[i + 2] == "3" and s[i + 3] == "4":
#             answer = False
#         elif s[i] == "1" and s[i + 1] == "2" and s[i + 2] == "3" and s[i + 3] == "4":
#             answer = True    
#     return answer

def solution(s):
    if (len(s) in [4, 6] and all(list(map(lambda x: ord(x) >= 48 and ord(x) <= 57, s)))):
        return True
    return False