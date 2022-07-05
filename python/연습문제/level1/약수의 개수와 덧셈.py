"""
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
"""

def solution(left, right):
    answer = 0
    
    for number in range(left, right + 1):
        index = 1
        count = 0
        while index <= number:
            if number % index == 0:
                count += 1
            index += 1
        if count % 2 == 0:
            answer += number
        else:
            answer -= number
    
    return answer
    
    

# def solution(left, right):
#     answer = 0
#     l = left
#     r = right
#     for i in range(r - l):
#         a = 0
#         b = 0
#         for j in range(l, r + 1):
#             for k in range(1, j + 1):
#                 if j % k == 0:
#                     a += 1
#                     b = j
#                     # print(b)
#         if a % 2 == 0:
#             answer += b
#         elif a % 2 != 0:
#             answer -= b
#         print(answer)    
#     return answer