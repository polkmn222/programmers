"""
문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
"""

def solution(n):
    answer = 0
    n = str(n)
    a = list(n)
    # print(a)
    a = list(map(int, a))
    answer = sum(a)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer