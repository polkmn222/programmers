"""
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
"""

def primenumber(x):
    for i in range(2, x):	# 2부터 x-1까지의 모든 숫자
    	if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
        	return False
    return True

def solution(nums):
    answer = 0
    result = []
    leng = len(nums)
    for i in range(leng):
        for j in range(i+1, leng):
            for k in range(j+1, leng):
                result.append(nums[i] + nums[j] + nums[k])
    
    # print(result)
    for i in result:
        if primenumber(i) == True:
                    answer += 1
    # result = set(result)
    # print(result)
    # for i in range(len(result)):
    #     cnt = 0
    #     for j in range(1, i+1):
    #         # print(i, j)
    #         if i % j == 0:
    #             cnt += 1
    #     if cnt == 2:
    #         answer += 1
    return answer
    
#     a = sorted(nums)
#     for i in a:
#         b += i
#         if b
    
#     return answer

#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     # print('Hello Python')
#     for i in range(len(nums)):
#         # a = 0
#         c = 0
#         for j in range(i, len(nums)):
#             for k in range(i+1, len(nums)):
#                 a = 0
#                 a = i + j + k
#                 b = 1
#                 while b <= a:
#                     if a % b == 0:
#                         c += 1
#         if c == 2:
#             answser += 1

    # return answer