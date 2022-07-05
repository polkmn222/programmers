"""
문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
"""

import numpy as np
def solution(A, B):

    return (np.matrix(A) * np.matrix(B)).tolist()

# def solution(arr1, arr2):
#     answer = [[0 for i in range(len(arr2[0]))] for j in range(len(arr1))]
#     # print(answer)
#     for i in range(len(arr1)):
#         for j in range(len(arr2[0])):
#             result = 0
#             for k in range(len(arr1[0])):
#                 answer[i][j] += arr1[i][k] * arr2[k][j]
                
#     return answer                

# import numpy
# def solution(arr1, arr2):
#     answer = [[]]
#     for x in range(len(arr2)):
#         a = [a*b for a,b in zip(arr1[x],arr2[x])]
#         print(a)
#     # mult_list = [arr1[i] * arr2[i] for i in range(len(arr1))]
#     # a = [x*y for x,y in zip(arr1, arr2)]
#     # print(a)
#     # arr1 = numpy.array(arr1)
#     # arr2 = numpy.array(arr2)
#     # newarr = arr1 * arr2
#     # newarr = numpy.multiply(arr1, arr2)
#     # print(newarr)
#     return answer