"""
문제 설명
다음 코드는 list1과 list2가 모두 list클래스의 인스턴스인지를 검사합니다. 코드의 빈칸을 채워넣어 정상 동작하도록 만들어 보세요.

인스턴스가 특정 클래스의 인스턴스인지 알아보는 방법으로 isinstance를 이용할 수 있습니다.
아래의 코드를 참고하여 문제를 해결해 보세요.

list1 = list("hello")
list2 = list("hello")

isinstance(list1, list)      #True
isinstance(list2, list)      #True
"""

list1 = list(range(10))
list2 = [1, 2, 3]

if isinstance( list1, list) and isinstance( list2, list):
    print("list1과 list2는 둘 다 list클래스 입니다.")