"""
문제 설명
다음 코드를 실행해서 어느 경우 if문 안의 코드가 실행되는지 확인해 보세요.

true와 false 논리연산은 아래와 같이 이루어 질 수도 있습니다.

구분	False	True
숫자	숫자 0	숫자 0을 제외한 모든 수
문자열	빈 문자열('')	빈 문자열을 제외한 모든 문자열
리스트	빈 리스트([])	빈 리스트를 제외한 모든 리스트
딕셔너리	빈 딕셔너리({})	빈 딕셔너리를 제외한 모든 딕셔너리
기타	None 오브젝트	
예를 들어,

bool(0)    #False
bool(3.3)  #True
bool([])    #False
bool(None)    #False
"""

if []:
    print("[]은 True입니다.")

if [1, 2, 3]:
    print("[1,2,3]은/는 True입니다.")

if {}:
    print("{}은 True입니다.")

if {'abc': 1}:
    print("{'abc':1}은 True입니다.")

if 0:
    print("0은/는 True입니다.")

if 1:
    print("1은 True입니다.")