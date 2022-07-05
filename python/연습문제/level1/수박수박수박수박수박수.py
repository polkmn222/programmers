"""
문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
"""

def solution(n):
    answer = ''
    a = "수박"
    for i in range(1, n+1):
        if i % 2 != 0:
            answer += a[0]
        else:
            answer += a[1]
    return answer