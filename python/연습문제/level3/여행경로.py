"""
문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
"""

from collections import defaultdict

def solution(tickets):
    r = defaultdict(list)
    
    for i, j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()
        
    s = ['ICN']
    p = []
    while s:
        q = s[-1]
        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())
            
    answer = p[::-1]
    
    return answer
        

# from collections import defaultdict

# def solution(tickets):
#     answer = []
#     # defaultdict로 하면 되고 dict로 하면 안됨 ;;
#     graph = defaultdict(list)
#     for t in tickets:
#         graph[t[0]].append(t[1])

#     for key in graph:
#         graph[key].sort()

#     def dfs(node, path):
#         if len(path) == len(tickets) + 1 :
#             return path

#         for i, city in enumerate(graph[node]):
#             graph[node].pop(i)

#             newPath = path[:]
#             newPath.append(city)

#             result = dfs(city,newPath)
#             if result : return result

#             graph[node].insert(i,city)


#     answer = dfs('ICN',['ICN'])

#     return answer