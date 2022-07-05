"""
문제 설명
product_list에는 상품의 목록이 들어 있고, price_list에는 각 상품의 가격이 순서대로 들어있습니다. 딕셔너리 컴프리헨션을 이용해서 product_dict를 상품의 이름을 키로 가지고, 가격을 값으로 가지는 딕셔너리로 만들어보세요.

Dictionary Comprehension을 이용한 문제입니다.

students = ["태연", "진우", "정현", "하늘", "성진"]
{"{}번".format(number):name for number, name in enumerate(students)}
    # {'2번': '정현', '0번': '태연', '1번': '진우', '4번': '성진', '3번': '하늘'}
students = ["태연", "진우", "정현", "하늘", "성진"]
scores = [85, 92, 78, 90, 100]
result = {x : y for x, y in zip(students, scores)}
    # {'성진': 100, '진우': 92, '하늘': 90, '태연': 85, '정현': 78}
zip은 두 개 이상의 리스트나 스트링을 받아서 인덱스에 맞게 자료를 묶어주는 역할을 합니다.
"""

product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = {x : y for x, y in zip(product_list, price_list)}


print(product_dict)