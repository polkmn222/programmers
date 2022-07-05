"""
문제 설명
코드 5번째 줄의 빈칸을 채워넣어 while문이 numbers의 값을 한 줄씩 출력하도록 만들어 보세요.

※ 빈칸은 length 변수를 이용해 채워주세요.

while문은 조건이 참인 경우 실행문을 반복하는 반복문입니다. 예제를 살펴보고 조건식의 빈칸을 올바르게 채워 보세요.

while 3<5:         # 3<5가 참이므로
    print("true")  # 이 코드가 반복적으로 실행됩니다.
"""

numbers = [1,2,3]
length = len(numbers)
i = 0
while length > i:
    print(numbers[i])
    i = i + 1