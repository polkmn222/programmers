"""
문제 설명
x = 3 ,     y = 5
의 값을 가지고 있습니다. position이 x와 y값으로 이루어진 튜플이 되도록 packing해 보세요.

packing이란 하나의 변수에 여러개의 값을 넣는 것입니다.
예를 들어,

a, b = 1, 2
c = a, b      #c = (1, 2)
"""

x = 3
y = 5

position = x, y

print("x, y로 이루어진 튜플 position의 값은 {}입니다.".format(position))