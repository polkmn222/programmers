"""
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
"""

from itertools import permutations

def solution(numbers):
    answer = 0
    nums = [i for i in numbers]
    a = []
    
    for i in range(1, len(numbers) + 1):
        a += list(permutations(nums, i))
        
    b = [int(("").join(p)) for p in a]
    c = list(set(b))
    
    for i in c:
        if i >= 2:
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                answer += 1
    
    return answer