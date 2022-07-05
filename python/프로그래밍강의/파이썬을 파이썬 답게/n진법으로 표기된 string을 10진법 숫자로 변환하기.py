"""
문제 설명
base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.

입력 설명
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 num을 나타내며, 두 번째 숫자는 base를 나타냅니다.

출력 설명
base 진법으로 표기된 num을 10진법 숫자로 출력해보세요.
"""

num, base = map(int, input().strip().split(' '))
# print(num + base)
print(int(str(num), base))