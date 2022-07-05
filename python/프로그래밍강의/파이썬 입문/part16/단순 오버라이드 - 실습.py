"""
문제 설명
Truck클래스는 Car클래스의 자식클래스입니다. Car클래스에 정의된 run을 Truck클래스에서 오버라이드해서 run을 실행하면 "트럭이 달립니다."라고 출력되도록 만들어 보세요.

오버라이드란 같은 이름을 가진 메소드를 엎어 쓴다는 의미입니다.
예를 들어,

class Animal( ):
    def greet( self ):
        print( "인사한다" )

class Human( Animal ):
    def greet( self ):
        print( "손을 흔든다" )

class Dog( Animal ):
    def greet( self ):
        print( "꼬리를 흔든다" )
이 때, Human과 Dog의 greet메소드는 부모의 greet메소드를 오버라이드 했다고 할 수 있습니다.
"""

class Car():
    
    def run(self):
        print("차가 달립니다.")


class Truck(Car):
    
    def run(self):
        print("트럭이 달립니다.")
    # 이 아래에서 run 메소드를 오버라이드 하세요.
    
    
truck = Truck()
truck.run()