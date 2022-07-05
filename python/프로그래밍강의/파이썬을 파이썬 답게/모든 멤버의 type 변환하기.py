"""
문제 설명
문자열 리스트 mylist를 입력받아, 이 리스트를 정수형 리스트로 바꾼 값을 리턴하는 함수, solution을 만들어주세요. 예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 [1, 100, 33] 을 리턴하면 됩니다.
"""

def solution(mylist):
    # answer = [int(i) for i in mylist]
    answer = list(map(int, mylist))
    return answer