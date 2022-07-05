"""
문제 설명
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
"""

def solution(n):
    answer = 0
    a = s3(n, 3)
    a = a[::-1]
    a = int(a, 3)
    answer = a
    print(a)
    return answer


def s3(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    
    
