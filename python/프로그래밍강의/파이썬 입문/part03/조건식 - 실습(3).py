"""
문제 설명
매 6시간마다 종이 울리는 시계를 구현하기 위해 hour에 저장된 현재 시간이 0,6,12,18시(6의 배수)일때만 코드8번째줄의 print문이 실행되도록 코드7번째줄에 if문을 추가하세요.

% remainder
%는 어떠한 값을 나누고 난 나머지를 구해주는 연산자 입니다. %를 이용하여 문제를 해결해 보세요.
예를 들어,

33 % 4 = 1
5 % 3 = 2
이처럼 쓰일 수 있습니다.
"""

#아래 두 줄의 코드는 변수 hour에 현재 시간을 저장합니다.
#이 코드가 어떻게 동작하는지는 이후 강의에서 다룹니다.
from datetime import datetime 
hour = datetime.now().hour

#현재 시간이 6의 배수일 때만 print문이 실행되도록 아래줄에 if문을 추가하세요
if hour % 6 == 0:
    print('종이 울립니다.')#if문을 추가한 이후 이 줄은 들여쓰기 되어야 합니다.