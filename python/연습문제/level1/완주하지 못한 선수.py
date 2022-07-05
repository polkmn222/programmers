"""
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
"""

def solution(participant, completion):
    answer = ''
    # p = participant
    # c = completion
    # # p.sort()
    # # c.sort()
    # for i in p:
    #     if i not in c:
    #         answer += i
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer=participant[i]
            return answer

    answer = participant[-1]
    
    return answer
    
    # print(p)
    # print(c)
    # answer = p^c
    # a = list(set(p) - set(c))
    # answer = str(a)
    # print(p.difference(c))
    # return str(answer)
    
#     for i in range(len(p)):
#         for j in range(len(c)):
#             if p[i] == c[j]:
#                 # p.remove(i)
#                 del p[0]
                
#     answer = p[0]
#     return answer
    # for i in range(len(participant)):
        # for j in range()
    # for i in participant:
    # # for i in range(len(participant)):
    #     for j in completion:
    #     # for j in range(len(completion)):
    #         if i == j:
    #             # participant.remove(participant[i-1])
    #             # answer = 0
    #             # del participant[j]
    #             # participant.pop()
    #             # continue
    #             participant.remove(i)
    # # answer = participant
    # answer = participant[0]
    # return answer