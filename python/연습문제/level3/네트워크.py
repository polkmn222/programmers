"""
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
"""

def solution(n, computers):
    answer = []
    for i in range(n):
        answer.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if answer[k] == answer[i]:
                        answer[k] = answer[j]
                        
    return len(set(answer))                    

# def solution(n, computers):
    
#     def DFS(i):
#         visited[i] = 1
#         for a in range(n):
#             if computers[i][a] and not visited[a]:
#                 DFS(a)
                
#     answer = 0
#     visited = [0 for i in range(len(computers))]
#     for i in range(n):
#         if not visited[i]:
#             DFS(i)
#             answer += 1
#     return answer