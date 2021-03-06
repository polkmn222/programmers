"""
문제 설명
a의 값은 5, b의 값은 7입니다. 코드 6~7번째 줄을 보면 result에 a와 b를 더한 값을 저장하고 결과를 출력하는데요, 이 부분을 함수로 만들어 보세요. 함수의 이름은 add로 만들어야 합니다. 함수를 만들고 나면 함수를 사용해서 결과가 출력되도록 하세요.

함수를 만들어봅시다. 아래의 예는 함수를 정의하고 호출하는 코드입니다. 예제를 참고하여 문제를 해결해 보세요.

def function():         # 함수의 정의
    print('안녕, 함수!')

print('첫줄 실행')
function()          # 함수의 호출
print('끝줄 실행')
이 코드의 출력값은 아래와 같습니다.

첫줄 실행
안녕, 함수!
끝줄 실행
"""

a = 5
b = 7

#이 아래줄에 a와 b를 더해서 result에 저장하는 함수add를 만들어 보세요.
def add(a, b):
    result = a + b #함수 내부의 코드가 되려면 이 줄은 들여쓰기 되어야 합니다.
    return result

print(add(a, b)) #함수 내부의 코드가 되려면 이 줄은 들여쓰기 되어야 합니다.
#이 아래에서 add함수를 사용해 보세요.