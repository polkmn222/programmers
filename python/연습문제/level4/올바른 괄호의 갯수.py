"""
문제 설명
올바른 괄호란 (())나 ()와 같이 올바르게 모두 닫힌 괄호를 의미합니다. )(나 ())() 와 같은 괄호는 올바르지 않은 괄호가 됩니다. 괄호 쌍의 개수 n이 주어질 때, n개의 괄호 쌍으로 만들 수 있는 모든 가능한 괄호 문자열의 갯수를 반환하는 함수 solution을 완성해 주세요.
"""

def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

def solution(n):
    answer = fac(2*n) / (fac(n+1) * fac(n))
    return answer