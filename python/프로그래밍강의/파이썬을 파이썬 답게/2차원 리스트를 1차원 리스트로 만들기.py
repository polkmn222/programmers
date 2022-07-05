"""
문제 설명
문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.
"""

def solution(mylist):
    # answer = []
    # for i in mylist:
    #     answer.append(mylist)
    answer = sum(mylist, [])
    return answer