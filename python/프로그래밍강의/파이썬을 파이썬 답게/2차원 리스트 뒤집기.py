"""
문제 설명
다음을 만족하는 함수, solution을 완성해주세요.

solution 함수는 이차원 리스트, mylist를 인자로 받습니다
solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우, solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.
"""

# def solution(mylist):
#     answer = list(map(list, zip(*mylist)))
#     return answer

def solution(mylist):
    answer=[]
    for i in range(len(mylist)):
        answer.append([])
        for j in range(len(mylist)):
            answer[i].append(mylist[j][i])

    return answer


# def solution(mylist):
#     answer = [[], [], []]

#     for i in range(0, len(mylist)):
#         for m in range(0, len(mylist[i])):
#             answer[i].append(mylist[m][i])
#     print(answer)
#     return answer

# def solution(mylist):
#     answer = [[]]
#     # for i in range(len(mylist)):
#     #     answer[0].append(i)
#     for i in range(len(mylist)):
#         for j in range(len(mylist[i])):
#             # answer[i].append[i][j]
#             answer[i].append(mylist[j][i])
#         # answer.append(i)
      
        
        
#     return answer