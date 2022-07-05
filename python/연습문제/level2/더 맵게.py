"""
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
"""

import heapq as hq

def solution(scoville, K):
    answer = 0
    
    hq.heapify(scoville)
    a = []
    b = 0
    
    while scoville:
        
        if scoville[0] >= K and not a:
            return b
        a.append(hq.heappop(scoville))
        
        if len(a) == 2:
            b += 1
            total = a[0] + a[1] * 2
            
            a = []
            hq.heappush(scoville, total)
            
    return -1        
    
# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     while True:
#         a = []
#         b = scoville[0] + (scoville[1] * scoville[1])
#         a.append(b)
#         for i in range(2, len(scoville)):
#             a.append(i)
#         a.sort()
#         answer += 1
#         if a[0] > K:
#             break
    
#     return answer