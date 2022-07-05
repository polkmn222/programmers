"""
문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
"""

def solution(a, b):
    answer = 0
    l1 = []
    if a < b:
        for i in range(a, b+1):
            l1.append(i)
        l2 = set(l1)
        answer = sum(l2)
    elif a == b:
        answer = a
    else:
        for i in range(b, a+1):
            l1.append(i)
        l2 = set(l1)
        answer = sum(l2)
    # elif a < b:
    #     for i in range(a-1, b, -1):
    #         l1.append(i)
    #     l1 = set(l1)
    #     answer = sum(l1)
    return answer