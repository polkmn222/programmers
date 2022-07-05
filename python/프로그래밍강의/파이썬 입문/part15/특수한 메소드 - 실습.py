"""
문제 설명
다음 코드는 완성된 Human클래스입니다. 19번째 줄에서 person을 Human클래스의 인스턴스로 만들고, person이 2번 걷고 1번 먹도록 만들어 보세요.

특수한 메소드에 대해 알아봅시다.

class Human( ):
    '''인간'''
    def __init__( self, name, weight ):
        '''초기화 함수'''
        self.name = name
        self.weight = weight

    def __str__( self )
        '''문자열화 함수'''
        return "{} ( 몸무게 {}kg )".format( self.name, self.weight )

person = Human( "사람", 60.5 )     # 초기화 함수 사용
print( person )                    # 문자열화 함수 사용
위 예에서의 초기화 함수 __init__은 매개변수를 받을 수 있게 정의되어 있습니다. 이 __init__함수에 매개변수를 넘겨주는 방법은 Human의 인스턴스를 만들때 괄호 안에 매개변수의 값을 넣어주는 것입니다.
"""

class Human():
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
    
    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

# 아래에서 person을 이름과 몸무게를 가지는 Human클래스의 인스턴스로 만들어보세요.

person = Human("psy", 60.0)
person.walk()
person.walk()
person.eat()

# print(person.walk)
# print(person)