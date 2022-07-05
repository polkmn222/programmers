"""
문제 설명
safe_index함수는 mylist와 value를 매개변수로 받아, mylist에서 value의 인덱스를 return하는 함수입니다. safe_index함수를 완성해 보세요. 단, value가 my_list안에 없으면 None을 리턴해야 합니다.

list에서 값을 이용하여 위치를 찾으려면 index()를 사용하세요.

예를 들어,

list1 = [135, 462, 27, 2753, 234]
print(list1.index(27))   #2가 출력됩니다.
index()에서 에러가 발생하지 않도록 처리하려면 value가 my_list안에 있는지 미리 확인하거나, try/except문을 활용하세요.
"""

def safe_index(my_list, value):
    # 함수를 완성하세요
    if value in my_list:
        return my_list.index(value)

    else:
        return None



print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))