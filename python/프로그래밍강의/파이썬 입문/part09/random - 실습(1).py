"""
문제 설명
https://docs.python.org/3.5/library/random.html#random.choice 에서 random.choice의 활용법을 확인하고, 3번째 줄에 코드를 추가해서 random_element가 list의 element중 하나를 가지도록 만들어 보세요.

공식 문서를 참고해 문제를 해결해 보세요.
필요한 내용을 둘러보고 싶을 때, 파이썬 내장 모듈과 함수의 정보가 필요 할 때 참고할 수 있습니다.
"""

import random
list = ["빨","주","노","초","파","남","보"]
random_element = random.choice(list)


print(random_element)