"""
문제 설명
다음 코드는 문구점 3곳을 검사하면서 풀이 있으면 문구점의 이름과 가격을 출력하고 MyException을 raise해서 즉시 for in문 전체를 종료합니다. 코드의 2번째 줄에 Exception클래스를 상속받는 MyException이라는 예외 클래스를 만들어 보세요.

사용자가 직접 예외를 정의하면, 오류 처리를 쉽게 할 수 있습니다.
예를 들어,

class BadUserName(Exception):             # 이름에 대한 예외처리
class PasswordNotMatched(Exception):      # 패스워드에 대한 예외처리

try:
    sign_up( )
except BadUserName:
    print( "이름으로 사용할 수 없는 입력" )
except PasswordNotMatched:
    print( "입력한 패스워드 불일치")
이 처럼 예외를 BadUserName, PasswordNotMatched으로 각각 처리해 줌으로써 코드의 직관성을 높일 수 있는 것이죠.
"""

# 이 아래에 Exception을 상속 받는 MyException클래스를 정의하세요.

class MyException(Exception):
    pass

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product == '풀':
                print("{}: {}원".format(shop, price))
                raise MyException
except MyException:
    print("풀을 찾았습니다.")