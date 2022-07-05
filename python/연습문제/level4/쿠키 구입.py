"""
문제 설명
과자를 바구니 단위로 파는 가게가 있습니다. 이 가게는 1번부터 N번까지 차례로 번호가 붙은 바구니 N개가 일렬로 나열해 놨습니다.

철수는 두 아들에게 줄 과자를 사려합니다. 첫째 아들에게는 l번 바구니부터 m번 바구니까지, 둘째 아들에게는 m+1번 바구니부터 r번 바구니까지를 주려합니다. 단, 두 아들이 받을 과자 수는 같아야 합니다(1 <= l <= m, m+1 <= r <= N). 즉, A[i] 를 i번 바구니에 들어있는 과자 수라고 했을 때, A[l]+..+A[m] = A[m+1]+..+A[r] 를 만족해야 합니다.

각 바구니 안에 들은 과자 수가 차례로 들은 배열 cookie가 주어질 때, 조건에 맞게 과자를 살 경우 한 명의 아들에게 줄 수 있는 가장 많은 과자 수를 return 하는 solution 함수를 완성해주세요. (단, 조건에 맞게 과자를 구매할 수 없다면 0을 return 합니다)
"""

from itertools import accumulate

def solution(cookie):
    answer = 0

    for i in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:i+1])))
        b = set(accumulate(cookie[i+1:]))
        c = a & b
        
        if c:
            answer = max(*c, answer)
            
    return answer        



# def solution(cookie):
#     answer = 0
#     n = len(cookie)
    
#     for i in range(n - 1):
#         ls, li = cookie[i], i
#         rs, ri = cookie[i + 1], i + 1
        
#         while True:
#             if ls == rs:
#                 answer = max(answer, ls)
                
#             if li > 0 and ls <= rs:
#                 li -= 1
#                 ls += cookie[li]
#             elif ri < n - 1 and rs <= ls:
#                 ri += 1
#                 rs += cookie[ri]
#             else:
#                 break
    
    
#     return answer