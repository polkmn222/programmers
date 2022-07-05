"""
문제 설명
gender의 값을 검사해서 "남자"라면 "남자입니다."라고 출력하고 "여자"라면 "여자입니다."라고 출력하고, 둘 다 아닐경우 "논바이너리입니다."라고 출력하도록 만들어 보세요.
if, elif, else를 이용해야 합니다.

elif
else와 if의 결합으로, 조건이 맞지 않는 경우 다른 경우를 검사합니다.
예를 들어,
if mine == SCISSOR:
    result = '가위'      # 조건이 참일 때 실행
elif mine == ROCK:
    result = '바위'      # 다른 조건이 참일 때 실행
else:
    result = '나머지'    # 조건이 거짓일 때 실행
"""

gender = "남자"
#이 아래줄에 if문을 추가하세요
if gender == '남자':
    
    print("남자입니다.")
#이 아래줄에 elif문을 추가하세요
elif gender == '여자':
    
    print("여자입니다.")
#이 아래줄에 else문을 추가하세요
else:
    
    print("논바이너리입니다")