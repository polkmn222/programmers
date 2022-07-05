"""
문제 설명
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
"""

def solution(s):
    answer = 0
    for i in s:
        if i == '(':
            answer += 1
        elif i == ')':
            answer -= 1
            if answer < 0:
                return False
    return answer == 0        

# def solution(s):
#     x = 0
#     for w in s:
#         if x < 0:
#             break
#         x = x+1 if w=="(" else x-1 if w==")" else x
#     return x==0
# def solution(s):
#     answer = True
#     # a = '('
#     # b = ')'
    
#     a = 0
#     b = 0
    
#     for i in s:
#         if i == '(':
#             a += 1
#         if i == ')':
#             b += 1
#         # print(a, b)    
    
#     # print(s[-1])
    
#     if a != b or s[-1] == '(':
#         answer = False
    
#     # print(count(a))
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     # print('Hello Python')

#     return answer