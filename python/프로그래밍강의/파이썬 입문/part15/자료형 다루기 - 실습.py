"""
문제 설명
자료형을 확인하는 방법에 대해 알아봅시다. 다음 코드의 실행 결과를 확인해 보세요.

type(변수명)을 이용하면 변수의 자료형을 알 수 있어요.

s = "Hello"
f = 3.14
i = 42
type(s)        # <class 'str'>
type(f)        # <class 'float'>
type(i)        # <class 'int'>
또한, isinstance(값, 자료형)을 이용하면 값에 대한 자료형이 참인지 거짓인지 알 수 있어요.

isinstance(3, int)               #True
isinstance(3.0, int)             #False
isinstance(3.2, float)           #True
isinstance("world", str)         #True
"""

my_list = [1, 2, 3]
my_dict = {"풀": 800, "색연필": 3000}
my_tuple = (1, 2, 3)
number = 10
real_number = 3.141592

print(type(my_list))
print(type(my_dict))
print(type(my_tuple))
print(type(number))
print(type(real_number))