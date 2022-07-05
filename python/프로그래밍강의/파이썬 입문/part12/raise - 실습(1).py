"""
문제 설명
다음 코드는 문구점 3곳을 검사하면서 풀이 있으면 문구점의 이름과 가격을 출력합니다.
실행 버튼을 눌러서 출력 결과를 확인해 보세요.
"""

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

for shop, products in shops.items():
    for product, price in products.items():
        if product =='풀':
            print("{}: {}원".format(shop, price))