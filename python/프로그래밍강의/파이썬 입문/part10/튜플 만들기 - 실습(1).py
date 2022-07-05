"""
문제 설명
튜플은 여러가지 방식으로 만들수가 있습니다. 다음 코드를 실행해서 튜플이 만들어질 수 있는 다양한 방법을 확인해 보세요.
"""

tuple1 = (1,2,3)
tuple2 = 1,2,3
list3 = [1,2,3]
tuple3 = tuple(list3)

if tuple1 == tuple2 == tuple3:
    print("tuple1과 tuple2와 tuple3은 모두 같습니다.")