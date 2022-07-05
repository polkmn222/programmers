"""
문제 설명
문자열 리스트 mylist를 입력받아, 이 리스트의 원소를 모두 이어붙인 문자열을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 '110033'을 리턴하면 됩니다.
"""

def solution(mylist):
    answer = ''
    # for i in range(len(mylist)):
    #     answer += mylist[i]
    answer = ''.join(mylist)
    return answer