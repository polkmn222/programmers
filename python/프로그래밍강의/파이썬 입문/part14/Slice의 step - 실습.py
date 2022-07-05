"""
문제 설명
주석의 지시에 따라 코드를 완성해 보세요.

step을 이용하면 slice한 값의 범위에서 step값을 주어 그 값만큼 건너뛰어 가져올 수 있습니다.
list[시작값 : 끝값 : step] 이러한 형식으로 사용할 수 있습니다.

예를 들어,

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list[2:8:2]          # [3, 5, 7]이 출력됩니다.
"""

list1 = list(range(20))

# new_list가 5, 8, 11, 14의 값을 가지도록 list1을 slice하세요
new_list = list1[5:15:3]

print(new_list)

# reverse_list가 17, 13, 9, 5의 값을 가지도록 list1을 slice하세요
reverse_list = list1[17:4:-4]

print(reverse_list)