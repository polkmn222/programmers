"""
문제 설명
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

명령어	수신 탑(높이)
I 숫자	큐에 주어진 숫자를 삽입합니다.
D 1	큐에서 최댓값을 삭제합니다.
D -1	큐에서 최솟값을 삭제합니다.
이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.
"""

import heapq

def solution(operations):
    answer = []
    heap = []
    
    for data in operations:
        if data[0] == 'I':
            heapq.heappush(heap, int(data[2:]))
        else:
            if len(heap) == 0:
                pass
            elif data[2] == '-':
                heapq.heappop(heap)
            else:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)
        
    return answer    


# def solution(operations):
#     answer = [0, 0]
#     a = []
#     for i in range(len(operations)):
#         if operations[i][0:1] == 'I':
#             a.append(int(operations[i][2:]))
#         elif operations[i] == 'D 1':
#             # a.remove(max(a))
#             b = sorted(a)
#             a.pop()
#         elif operations[i] == 'D -1':
#             # a.remove(min(a))
#             b = sorted(a)
#             a.pop(0)
            
#     print(a)        
    
    
#     return answer
#     # a = []
#     # b = []
#     # for i in range(len(operations)):
#     #     if operations[i][0:1] == 'I':
#     #         a.append(operations[i][2:])
#     #     if operations[i][0:1] == 'D':
#     #         b.append(operations[i][2:])
#     # # print(a)
#     # # print(b)
#     # a = list(map(int, a))
#     # # a.sort()
#     # print(a)
#     # print(b)
#     # for i in range(len(b)):
#     #     if len(a) <=0:
#     #         break
#     #     # c = min(a)
#     #     # d = max(a)
#     #     if b[i] == '-1':
#     #         # a.remove(c)
#     #         # del a[0]
#     #         # print(1)
#     #         a.pop(0)
#     #     elif b[i] == '1':
#     #         a.pop()
#     #         # a.remove(d)
#     #         # del a[-1]
#     #         # print(2)
#     # print(a)        
#     # # answer[0] = max(a)
#     # # answer[1] = min(a)
#     # return answer