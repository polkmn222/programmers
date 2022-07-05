"""
문제 설명
Car클래스를 상속받는 Truck이라는 클래스를 만들고, load라는 메소드를 만들어 보세요. load메소드에서는 "짐을 실었습니다."라고 출력하면 됩니다.

Car클래스를 부모 클래스, Truck클래스를 자식 클래스로 만들어야 합니다.
예를 들어,

class Animal():
    def walk(self):
        print("걷는다")
class Human(Animal):
    def wave(self):
        print("손을 흔든다")
자식 클래스의 괄호에 부모 클래스의 이름을 채워 넣으면 부모 클래스를 상속 받게 됩니다.
"""

class Car():
    
    def run(self):
        print("차가 달립니다.")

# 아래에서 Car를 상속받는 Truck이라는 클래스를 만들고, load라는 메소드를 만들어 보세요.
# load메소드에서는 "짐을 실었습니다."라고 출력하면 됩니다.
class Truck(Car):
    
    def load(self):
        print("짐을 실었습니다.")
        
        