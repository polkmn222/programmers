"""
문제 설명
list1과 list2를 이용해서 [1,2,3,4,5,6]을 값으로 가지는 list3을 만들어 보세요.

리스트에 새로운 값을 추가하는 방법을 알아봅시다.

list1 = [1, 2]

list1.append(3)         # append를 이용 list1 = [1, 2, 3]

list2 = list1+[4]       # 뒤에 새로운 리스트 더하기 list2 = [1, 2, 3, 4]

list3 = list1 + list2   # list끼리 더하기 list3 = [1, 2, 3, 1, 2, 3, 4]
"""

list1=[1,2,3]
list2=[4,5,6]
list3 = list1 + list2

print(list3)