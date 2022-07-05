"""
문제 설명
스크린샷 2018-09-14 오후 5.44.19.png

위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.
"""

def solution(triangle):
    
    height = len(triangle)
    
    while height > 1:
        for i in range(height - 1):
            triangle[height-2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1
        
    answer = triangle[0][0]
    return answer

# def solution(triangle):
#     answer = triangle[0][0]
#     if len(triangle) == 2:
#         answer += max(triangle[1])
#     else:
#         l = len(triangle)
#         dp = [0] * l
#         dp[0] = triangle[0]
#         for i in range(1, l):
#             dp[i] = [0] * (i + 1)
#             for j in range(i + 1):
#                 if j == 0:
#                     dp[i][j] = dp[i-1][j] + triangle[i][j]
#                 elif j == i:
#                     dp[i][j] = dp[i-1][j-1] + triangle[i][j]
#                 else:
#                     dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
#         answer = max(dp[l-1])            
#     return answer
