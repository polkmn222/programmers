"""
문제 설명
n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.
"""

from collections import deque

def solution(n, edge):
    answer = 0
    # print(n)
    # print(edge)
    route = [0] * (n+1)
    edge.sort()
    queue = deque()
    graph = [[] for i in range(n+1)]
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    queue.append(1)
    route[1] = 1
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if route[i] == 0:
                queue.append(i)
                route[i] = route[now] + 1
    
    count = max(route)
    for i in route:
        if i == count:
            answer += 1
    
    
    return answer