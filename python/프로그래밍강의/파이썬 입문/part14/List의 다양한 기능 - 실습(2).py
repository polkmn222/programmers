"""
문제 설명
insert(), sort(), reverse()를 사용해서 다음 코드에 주석으로 적힌 내용을 만들어 보세요.

문제를 해결하기 위해 리스트의 기능에 대해 알아보아요.

list.insert(index, value) : 원하는 위치에 값을 추가합니다
list = [1, 2, 3]
list.insert(3, 4)     #list = [1, 2, 3, 4]로 4가 추가되었습니다.
list.sort() : 값을 순서대로 정렬
list = [3, 5, 6, 4, 2, 1]
list.sort()           #list = [1, 2, 3, 4, 5, 6]으로 정렬됩니다.
list.reverse() : 값을 역순으로 정렬
list = [3, 5, 6, 4, 2, 1]
list.reverse()     #list = [1, 2, 4, 6, 5, 3] 역순으로 정렬됩니다
"""

list1 = [1, 2, 3, 4]

# 아래줄에서 list1의 1번째 자리에 8을 넣고 원래 있던 값은 오른쪽으로 밀어 보세요.

list1.insert(0, 8)
print("첫 번째 자리에 8을 넣은 결과 : {}".format(list1))
# 아래줄에서 list1을 작은 수부터 큰 수로 정렬해 보세요

list1.sort()
print("list1을 작은 수부터 큰 수로 정렬한 결과 : {}".format(list1))
# 아래줄에서 list1을 거꾸로 만들어 보세요

list1.reverse()
print("list1을 거꾸로 정렬한 결과 : {}".format(list1))