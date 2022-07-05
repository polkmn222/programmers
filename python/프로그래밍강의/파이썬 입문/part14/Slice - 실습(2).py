"""
문제 설명
함수 substring은 문자열 str을 받아서 start부터 end 이전까지에 해당하는 문자열을 return하는 함수입니다. 코드의 2번째 줄의 빈칸을 채워 substring함수를 완성해 보세요. 단, slice를 이용해야 합니다.

예를 들어,

text = "hello world"
text[1:5]    # ello
text 문자열의 1번째부터 5번째 전까지인 ello가 출력되었습니다.
위의 예를 보면 다음과 같이 나타낼 수 있습니다.

text[a:b]    # a번째부터 b번째 전까지 반환
"""

def substring(text, start, end):
    return text[start:end]


my_text = "Hello world"
between_2_5 = substring(my_text, 2, 5)
print(between_2_5)