"""
문제 설명
코드의 6번째 줄에 else문을 추가해서 비기지 않은 경우에만 7번째 줄의 print문이 실행되도록 만들어 보세요.

else
if의 조건이 맞지 않는 경우 항상 실행됩니다.
반드시 if 뒤에 나와야 합니다.
예를 들어,
if mine == yours:   # 비기는 경우
    result = DRAW
else:               # 비기는 경우를 제외한 모든 경우
    result = '이기거나 지거나'
"""

mine = '가위'
yours = '바위'
if mine == yours:
    print("비겼습니다.")
else:
    
#이 아래줄에 else문을 추가해서 비기지 않은 경우에만 아래 print문이 실행되도록 만들어 보세요

    print("비기지 않았습니다.")#else문이 추가되고 나면 이 줄은 들여쓰기 되어야 합니다.