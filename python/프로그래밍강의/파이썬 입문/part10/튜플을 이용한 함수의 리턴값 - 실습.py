"""
문제 설명
products의 상품명과 값을 한 줄씩 출력하도록 코드의 4번째줄의 빈칸을 채워 보세요.

튜플로 리턴하기 위해 리스트나 딕셔너리를 이용할 수 있습니다. 딕셔너리의 items()를 이용하여 튜플을 리턴할 때에는 *를 사용할 수 있습니다. 아래의 예제를 살펴보고 문제를 해결해 보세요.

ages = {'Tod' : 35, 'Jane' : 23, 'Paul' : 62}

for a in ages.items():
    print('{}의 나이는:{}'.format(a[0], a[1]))

for a in ages.items():
    print('{}의 나이는:{}'.format(*a))    # 두 출력 결과가 같습니다.

"""

products = {"풀" : 800, "색종이": 1000}

for product_detail in products.items():
    print("{}의 가격: {}원".format( *product_detail ))