"""
문제 설명
birth_year와 birth_date를 활용해서 year_and_date가 생년월일에 해당하는 문자열을 가지도록 만들어 보세요.

예를 들어, birth_year가 1999이고, birth_date가 0326일 때
year_and_date가 19990326의 문자열을 가지도록 코드를 작성해 보세요.
"""

birth_year='1985'
birth_date='0502'
year_and_date = birth_year + birth_date

print("year_and_date : {}".format(year_and_date))