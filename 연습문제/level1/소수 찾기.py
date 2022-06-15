"""
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
"""

def solution(n):
    sieve = [True] * (n + 1)
    
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i * i, n+1, i):
                sieve[j] = False
                
    x = [i for i in range(2, n+1) if sieve[i] == True]
    answer = len(x)
    return answer

# def solution(n):
#     answer = 0
#     L=[]
#     for i in range(n):
#         L.append(1)
#     for a in range(n):
#         for b in range((2+a)*2,n,2+a):
#             L[b]=0
#     L[0]=0
#     L[1]=0
#     L[-1]=0
#     return L.count(1)

# def solution(n):
#     answer = 0
#     a = []
#     for i in range(n):
#         a.append(1)
#     for i in range(n):
#         for j in range((2+a)*2, n, 2+a):
#             a[j] = 0
#     a[0] = 0
#     a[1] = 0
#     a[-1] = 0
#     return a.count(1)

# from cmath import sqrt

# def solution(n):
#     prime = [2]
#     not_prime = []
#     answer = 1
#     l = [i for i in range(1, n+1)]
    
#     for i in range(1, n + 1):
#         if i < 3:
#             if i not in prime:
#                 not_prime.append(i)
#         else:
#             for j in prime:
#                 if j > int(sqrt(i).real):
#                     break
#                 if i % j == 0:
#                     not_prime.append(i)
#                     break
#         prime = list(set(l) - set(not_prime))            
    
#     return len(prime)

# def solution(n):
#     answer = 0
#     # for i in range(1, n+1):
#     #     a = 0
#     #     for j in range(1, n+1):
#     #         if i % j == 0:
#     #             a += 1
#     #     if a == 2:
#     #         answer += 1
#     #     # if a == 2:
#     #         # answer += 1
#     #     # print(answer)    
#     # answer = seive(n)
#     return answer

# def seive(n):
#     answer = 0
#     for i in range(1, n+1):
#         a = 0
#         for j in range(1, n+1):
#             if i % j == 0:
#                 a += 1
#         if a == 2:
#             answer += 1
#         # if a == 2:
#             # answer += 1
#         # print(answer)
#     return answer