"""
문제 설명
이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.
"""

import collections

my_str = input().strip()
answer = collections.Counter(my_str)
MAX = 0
MAX_str = ''
for x, a in answer.most_common(): 
    if a >= MAX:
        MAX = a
        MAX_str += x
MAX_str = ''.join(sorted(MAX_str))  
print(MAX_str)


# from collections import Counter
# import collections

# my_str = input().strip()

# answer = collections.Counter(my_str)
# print(answer)
# # counter = Counter(my_str)
# # # O(N) 소요
# # for i in range(1, 10):
# #     print(counter[i])
# # print(my_str)