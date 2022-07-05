"""
문제 설명
숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 사전순으로 리턴하는 함수 solution을 완성해주세요.
"""

from itertools import permutations 

def solution(mylist):
    answer = list(permutations(mylist))
    answer.sort()
    return answer