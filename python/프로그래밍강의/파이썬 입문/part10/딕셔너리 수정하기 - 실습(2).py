"""
문제 설명
days_in_month에는 엉뚱하게도 -1월이라는 이름표와 값이 있는데요. 이 값을 지워보세요. (단, 첫번째 줄은 수정하지 마세요)

아래의 예 처럼 딕셔너리를 수정할 수 있습니다.

dict['one' : 1, 'two' : 2]

dict['three'] = 3    # 값을 추가합니다  {'one' : 1, 'two' : 2, 'three' : 3}
dict['one'] = 11     # 값을 수정합니다  {'one' : 11, 'two' : 2, 'three' : 3}
del(dict['one'])     # 값을 삭제합니다  {'two' : 2, 'three' : 3}
dict.pop('two')      # 값을 삭제합니다  {'three' : 3}
"""

days_in_month = {"1월":31, "2월":28, "3월":31,"-1월":97889789}
days_in_month.pop("-1월")


print(days_in_month)