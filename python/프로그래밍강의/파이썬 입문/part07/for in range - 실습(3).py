"""
문제 설명
enumerate를 이용해서 무지개의 순서와 색을 출력하도록 빈칸을 채워보세요.

enumerate는 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 합니다. 아래의 예를 참고하여 문제를 해결해 보세요.

names = ['철수', '영희', '영수']
for i, name in enumerate(names):
    print('{}번 : {}'.format(i + 1, name))
이 예제의 출력값은 아래와 같습니다.

1번 : 철수
2번 : 영희
3번 : 영수
"""

rainbow=["빨","주","노","초","파","남","보"]
for i,color in enumerate(rainbow):
    print('{}번째 색은 {}'.format(i+1,color))