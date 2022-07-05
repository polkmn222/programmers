"""
문제 설명
list1과 list2는 같은 값을 가지는 리스트입니다. 코드의 4번째줄에 있는것과 같이 is연산을 하면 둘이 같은 인스턴스인지를 알아볼 수 있고, 7번째줄에 있는 ==연산을 하면 둘이 같은 값을 가지는지 알아볼 수 있습니다. 다음을 실행해서 나오는 출력을 확인하고 is연산과 ==연산의 차이를 확인해 보세요.

인스턴스는 클래스에 의해 생성된 객체를 뜻합니다. 인스턴스의 클래스가 같더라도 각자 다른 값을 가질 수 있습니다.

예를 들어,

list1 = list("hello")
list2 = list("hello")

isinstance(list1, list)      #True
isinstance(list2, list)      #True

print(list1 == list2)        #True     list1과 list2는 같은 값을 가집니다.
print(list1 is list2)        #False    list1과 list2는 다른 인스
"""

list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list1:
    print("당연히 list1과 list1은 같은 인스턴스입니다.")

if list1 == list2:
    print("list1과 list2의 값은 같습니다.")
    if list1 is list2:
        print("그리고 list1과 list2는 같은 인스턴스입니다.")
    else:
        print("하지만 list1과 list2는 다른 인스턴스입니다.")