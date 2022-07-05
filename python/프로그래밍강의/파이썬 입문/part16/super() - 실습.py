"""
문제 설명
Truck클래스는 Car클래스의 상속을 받는 자식클래스입니다. Truck클래스의 __init__에서 name, capacity(몇톤트럭인지)를 입력받아 인스턴스의 값으로 저장하세요. (단, Truck클래스의 __init__에서 name을 설정하는 부분은 super()를 이용해서 처리하도록 만드세요.)

자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우 super()를 이용합니다.

예를 들어,

class Animal( ):
    def __init__( self, name ):
        self.name = name

class Human( Animal ):
    def __init__( self, name, hand ):
        super().__init__( name )        # 부모클래스의 __init__ 메소드 호출
        self.hand = hand

person = Human( "사람", "오른손" )
위의 예처럼 Human클래스의 __init__에서 name을 super()로 처리할 수 있습니다.
"""

class Car():
    
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print("차가 달립니다.")


class Truck(Car):
    # 이 아래에서 __init__ 메소드를 오버라이드 하세요.
    def __init__( self, name, capacity ):
        super().__init__( name )        
        self.capacity = capacity
    def load(self):
        print("짐을 실었습니다.")