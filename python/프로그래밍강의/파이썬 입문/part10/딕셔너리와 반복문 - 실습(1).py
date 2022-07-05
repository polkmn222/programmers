"""
문제 설명
for in문을 이용해서 days_in_month의 이름표(key)를 한줄씩 출력해 보세요.

딕셔너리를 반복문에서 활용하는 방법을 알아봅시다. 딕셔너리의 반복문에서는 경우에 따라 key를 가져올 수도 있고 값을 가져올 수도 있습니다. 아래의 예를 참고하여 문제를 해결해 보세요.

ages = {'Tod' : 35, 'Jane' = 23, 'Paul' : 62}

for key in ages.keys():      # keys() 생략 가능
    print(key)               # Tod, Jame, Paul이 출력됩니다.

for value in ages.values():
    print(value)             # 62, 23, 35가 출력됩니다.
"""

days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

for i in days_in_month.keys():
    print(i)