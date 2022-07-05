"""
문제 설명
check_and_clear는 딕셔너리 타입의 box를 매개변수로 받는데요. 만약 box에 "불량품"이라는 이름표가 있으면 box 전체를 빈 딕셔너리로 만들어 버리고, 불량품이 없으면 box를 그대로 두는 함수입니다. 다음 코드를 수정해서 check_and_clear 함수를 완성하세요.

딕셔너리 타입에 키가 있는지 확인하려면 in을 사용해 보세요.
예를 들어, 딕셔너리에 'two'라는 키가 있는지 확인하려면

'two' in dict.keys()
또한 딕셔너리의 내용을 전부 삭제하고 싶다면 dict.clear()를 호출하면 된답니다.
"""

def check_and_clear(box):
    # print("불량품이 있으면 box를 clear합니다.")
    if '불량품' in box:
        box.clear()
    else:
        print(box)
        

box1 = {"불량품" : 10}
check_and_clear(box1)
# {}가 출력되어야합니다.
print(box1)

box2 = {"정상품": 10}
check_and_clear(box2)
# {"정상품": 10}가 출력되어야합니다.
print(box2)