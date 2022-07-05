"""
문제 설명
or연산의 결과는 앞의 값이 True이면 앞의 값을, 앞의 값이 False이면 뒤의 값을 따릅니다. 다음 코드를 실행해서 각각 a와 b에 어떤 값이 들어가는지 확인해 보세요.

예를 들어,

a = True or 1      #True   앞의 값이 True입니다.
b = False or 0     #0      앞의 값이 False이므로 뒤의 값을 따릅니다.
c = 0 or False     #False  앞의 값이 0이므로 False입니다. 따라서 뒤의 값인 False를 따릅니다.
d = 1 or False     #1      앞의 값이 1이므로 True입니다.
"""

a = 1 or 10    # 1의 bool 값은 True입니다.
b = 0 or 10    # 0의 bool 값은 False입니다.


print("a:{}, b:{}".format(a, b))