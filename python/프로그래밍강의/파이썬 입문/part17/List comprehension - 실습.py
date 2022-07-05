"""
문제 설명
list comprehension을 이용해서 list1이 1부터 100 사이의 8의 배수를 가지도록 만들어 보세요.

list comprehension의 예를 들어 봅시다.

areas1 = [ i*i for i in range(1,11) ]                          # [ 계산식 for문 ]
areas2 = [ i*i for i in range(1,11) if i % 2 == 0]             # [ 계산식 for문 조건문 ]
areas3 = [ ( x, y ) for x in range(15) for y in range(15) ]    # [ 계산식 for문 for문 ]
"""

list1 = [i for i in range(1, 101) if i % 8 == 0]


print("list1 : ", list1)