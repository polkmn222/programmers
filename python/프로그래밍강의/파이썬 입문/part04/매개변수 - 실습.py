"""
문제 설명
함수 add는 매개변수로 a와 b를 받고 있습니다. 코드의 3번째 줄을 수정해서 result에 a와 b를 더한 값을 저장하고 출력되도록 만들어 보세요.

매개변수를 받는 함수를 만들고 사용하는 문제입니다. 아래의 예제를 참고하여 문제를 해결해 보세요.

def print_round(number):    # number를 매개변수로 하는 함수 정의
    rounded = round(number)
    print(rounded)  

print_round(4.6)            # 함수의 호출
print_round(2.2)
"""

def add(a,b):
    #함수 add에서 a와 b를 입력받아서 두 값을 더한 값을 result에 저장하고 출력하도록 만들어 보세요.
    result = a + b
    print( "{} + {} = {}".format(a,b,result) )#print문은 수정하지 마세요.

add(10,5)