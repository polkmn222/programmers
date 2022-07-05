"""
문제 설명
코드의 5번째 줄을 수정해서 days_until_christmas 함수가 오늘부터 2030년 12월 25일 사이에 몇일이 있는지를 리턴하도록 만들어 보세요.
(단, 시간단위는 고려하지 마세요.)

datetime은 -연산을 지원 합니다.
예를 들면,

start_time = datetime.datetime()
how_long = start_time - datetime.datetime.now()
이처럼 -연산을 이용해 start_time으로부터 how_long까지 얼마나 남았는지 구할 수 있습니다.
"""

import datetime

def days_until_christmas():
    # start_time = datetime.datetime(2022, 6, 24)
    christmas_2030 = datetime.datetime(2030, 12, 25)
    days = (christmas_2030 - datetime.datetime.now()).days
    return days


print("{}일".format(days_until_christmas()))