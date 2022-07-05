"""
문제 설명
days_in_month의 각 이름표와 값을 다음과 같은 형식으로 출력해 보세요.

1월은 31일이 있습니다.
2월은 28일이 있습니다.
...
정확한 출력 형식은 작성되어 있는 print함수를 참고하세요.

딕셔너리의 반복문에서는 key와 value를 선택해서 가져올 수 있었지요. 이번 문제처럼 key와 value를 둘 다 가져와야 할 때에는 items()를 사용하면 됩니다. 아래의 예를 참고하여 문제를 해결해 보세요.

ages = {'Tod' : 35, 'Jane' : 23, 'Paul' : 62}

for key, value in ages.items():
    print('{}의 나이는 {} 입니다'.format(key, value))
"""

days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

# for key, value in days_in_month.items():
#     print("{}은 {}일이 있습니다.".format(key, value)
#출력 형식은 아래 print함수를 참고하세요
# for i in days_in_month:
    # print("{}은 {}일이 있습니다.".format(days_in_month.keys(), days_in_month.values()) )

for key, value in days_in_month.items():
    print('{}은 {}일이 있습니다.'.format(key, value))