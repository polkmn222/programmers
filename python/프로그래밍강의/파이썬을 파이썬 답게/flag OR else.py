"""
문제 설명
본 문제에서는 자연수 5개가 주어집니다.

숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고
모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는
코드를 작성해주세요.
"""

import math

a = [int(input()) for i in range(5)]

answer = 'not found'
m = 1
for i in a:
    m *= i
    if math.sqrt(m) == int(math.sqrt(m)):
        answer = 'found'

print(answer)


# import math

# if __name__ == '__main__':
#     numbers = [int(input()) for _ in range(5)]
#     multiplied = 1
#     for number in numbers:
#         multiplied *= number
#         if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
#             print('found')
#             break
#     else:
#         print('not found')


# answer = 'not found'
# b = []
# for i in range(5):
#     a = int(input())
#     b.append(a)
    
# # print(b)

# for i in b:
#     if (i ** 0.5) % 1 == 0:
#         answer = 'found'
#         break
#     # else:
#     #     answer = 'not found'
        
# print(answer)        

# print(a)
# sqrt = a ** (1/2)
# if sqrt % 1 == 0:
#     answer = 'found'

# print(answer)
        
    


# def issquare(n):
# 	temp = n ** 0.5
# 	if int(temp) == temp:
# 		if temp ** 2 == n:
# 			return "found"
# 	return "not found"
# answer = ''
# b = []
# for i in range(5):
#     a = int(input())
#     b.append(a)
# print(answer)
# for i in range(len(b)):
	# temp = b[i] ** 0.5
	# if int(temp) == temp:
	# 	if temp ** 2 == b[i]:
	# 		return "found"
	# return "not found"
# print(b)
# for i in range(len(b)):
#     sqrt = i ** (1/2)
#     if sqrt % 1 == 0:
#         answer = "found"
#     answer = "not found"

# print(answer)