"""
문제 설명
풀을 파는 가게를 발견하면 for문 전체를 즉시 종료하고 싶습니다. for 문을 try/except로 감싸고 print문 다음에 raise StopIteration을 추가해서 풀을 파는 가게를 하나만 출력하도록 만들어 보세요. except문에서는 StopIteration을 지정해 주어야 합니다.

사용자는 여러가지 이유로 에러를 직접 발생시킬 수 있습니다. 그중 하나의 예로 중첩된 for 문에서 바로 종료하고 싶을 때 에러를 발생시키기도 합니다.
아래의 예를 참고하여 문제를 해결해 보세요.

try:
    ...
    raise 에러종류
    ...
except 에러종류:
    # 처리할 코드
"""

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product =='풀':
                print("{}: {}원".format(shop, price))
                raise StopIteration

except StopIteration:
    pass