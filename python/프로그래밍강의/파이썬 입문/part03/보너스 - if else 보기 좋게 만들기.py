"""
문제 설명
다음 코드는 mine과 yours의 값에 따라 가위바위보의 승패를 판정하고 있습니다. mine의 값이 "가위", "바위", "보"일때를 처리하는 부분이 점점 더 깊은 블록으로 들어가고 있어서 코드를 파악하기가 쉽지 않은데요. elif를 사용해서 코드를 정리해 보세요.

elif는 if와 else를 결합으로, 조건이 맞지 않는 다른 경우를 검사한다고 했었지요. 그렇다고 기능에 차이가 있는 것이 아닙니다. 코드가 눈에 어떻게 보이는지에 따른 선호의 차이이지요. 이를 참고하여 코드를 정리해 보세요.

if True:
    pass    # 조건이 참일 때 실행
elif False :
    pass    # 다른 조건이 참일 때 실행
else:
    pass    # 조건이 거짓일 때 실행
"""

mine = "가위"
yours = "바위"

if mine == yours:
    print("비김")
else:
    if mine == "가위":
        if yours == "보":
            print("이겼다")
        else:
            print("졌다")
    else:
        if mine == "바위":
            if yours == "가위":
                print("이겼다")
            else:
                print("졌다")
        else:
            if mine == "보":
                if yours == "바위":
                    print("이겼다")
                else:
                    print("졌다")