"""
문제 설명
다음 코드는 발생하는 예외를 try/except문으로 처리하고 있습니다. 5번째 줄에서는 어떤 에러가 발생하는지 출력할 수 있도록 빈칸을 채우고, 6번째 줄은 예외를 출력할 수 있도록 format의 빈칸을 작성하세요.

예외의 이름을 모르는 경우에는 Exception as를 통해 해결할 수 있습니다.

아래의 예를 참고하여 문제를 해결해 보세요.

try:
    # 에러가 발생할 가능성이 있는 코드
except Exception as ex:     # 에러 종류
    print('에러가 발생 했습니다', ex)  # ex는 발생한 에러의 이름을 받
"""

try:
    a = 5
    b = 0
    c = a / b
except Exception as ex:
    print('다음과 같은 에러가 발생했습니다: {}'.format( ex))