"""
문제 설명
taxi는 Car클래스의 인스턴스로 "택시"라는 이름을 가지고 있습니다.taxi.run()을 호출할 수 있도록 Car클래스 밖에 정의되어 있는 run함수를 클래스 안으로 가져오세요. 가져온 다음에는 run의 매개변수인 car를 self로 변경하세요.

메소드는 클래스에 포함되어 있는 함수를 가리킵니다.
함수를 클래스 안으로 가져오려면 그 함수를 클래스 안에 넣어 들여쓰고, 메소드의 첫 번째 인자를 self로 변경해야 합니다.

예를 들어,

class Human( ):
    '''인간'''
    def create( name, weight ): # 다음 강의에서 자세히 설명
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat( self ):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))
"""

class Car():
    '''자동차'''

    def run(self):
        print("{}가 달립니다.".format(self.name))

taxi = Car()
taxi.name = "택시"
taxi.run()