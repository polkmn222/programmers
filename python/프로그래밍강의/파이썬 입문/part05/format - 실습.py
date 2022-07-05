"""
문제 설명
변수 name과 color에 자신의 이름과 좋아하는 색상을 문자열로 입력하고 3번째줄 .format()의 괄호 안을 수정해서 자신의 이름과 좋아하는 색상을 출력해 보세요.

str.format()
문자열의 대괄호 자리에 format 괄호안의 값을 하나씩 넣습니다.
아래의 예를 참고하여 문제를 해결해 보세요.
number = 20
welcome = '환영합니다'
base = '{} 번 손님 {}'

# 아래 3개의 print는 같은 값을 출력합니다.
print(number,'번 손님',welcome)
print(base.format(number,welcome))
print('{} 번 손님 {}'.format(number,welcome))
# => 20 번 손님 환영합니다
"""

name = 'psy'
color = 'red'
print('안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'.format(name, color))