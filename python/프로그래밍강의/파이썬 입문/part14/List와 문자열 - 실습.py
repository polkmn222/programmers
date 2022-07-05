"""
문제 설명
다음 코드는 "오늘은 날씨가 흐림"이라는 문자열을 "오늘은 날씨가 맑음"이라는 문자열로 바꾸는 과정을 보여주고 있습니다. 코드의 안내를 따라 빈 부분을 작성해 보세요.

List와 String의 유사성을 이용해 보세요.
리스트와 문자열은 서로 변환할 수 있습니다.

예를 들어,

str = "10:35:27"
list = str.split(":")             #문자열을 ":"기준으로 리스트화
new_str = ":".join(list)          #리스트를 ":"기준으로 문자열화
이처럼 ":"을 기준으로 문자열과 리스트를 서로 변환 할 수 있습니다.
"""

str = "오늘은 날씨가 흐림"

# split()을 이용해서 str을 공백으로 나눈 문자열을 words에 저장하세요
words = str.split(" ")


# index()를 이용해서 "흐림"이 words의 몇번째에 있는지 찾고, 
# position에 저장하세요.
position = words.index("흐림")


words[position] = "맑음"

# join()을 이용해서 words를 다시 문자열로 바꿔 new_str에 저장하세요. 
# words를 문자열로 바꿀때는 공백 한 칸을 기준으로 붙이면 됩니다.
new_str = " ".join(words)


print(new_str)