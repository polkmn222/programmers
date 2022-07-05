"""
문제 설명
range를 이용해서 무지개의 순서와 색을 출력하도록 빈칸을 채워보세요. 단, rainbow에 새로운 값이 추가되더라도 그 값을 모두 출력할 수 있도록 len을 이용해야 합니다.

range 괄호에 len을 넣으면 리스트의 길이만큼 반복할 수 있습니다. 아래의 예를 참고하여 문제를 해결해 보세요.

names = ['철수', '영희', '바둑이', '귀도', '비단뱀']

for i in range(len(names)):
    name = names[i]
    print('{}번 : {}'.format(i + 1, name))
이 예제는 아래의 결과와 같습니다.

1번 : 철수
2번 : 영희
3번 : 바둑이
4번 : 귀도
5번 : 비단뱀
"""

rainbow=["빨","주","노","초","파","남","보"]
for i in range(len(rainbow)):
    color = rainbow[i]
    print('{}번째 색은 {}'.format(i+1,color))