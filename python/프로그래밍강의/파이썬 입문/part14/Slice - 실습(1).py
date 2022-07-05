"""
문제 설명
다음 지시를 따르도록 코드의 빈칸을 채워 보세요.

문제를 해결하기 위해 Slice를 해봅시다.

Slicing
리스트나 문자열에서 여러개의 값을 가져오는 기능입니다.
예를 들어,

text = "hello world"
text[1:5]         # ello          1번째부터 5번째 전까지
text[3:]          # lo world      3번째부터 끝까지
text[:3]          # hel           처음부터 3번째까지
text[:]           # hello world   처음부터 끝까지
"""

rainbow = ["빨", "주", "노", "초", "파", "남", "보"]

# red_colors가 ["빨", "주", "노"]의 값을 가지도록 rainbow를 slice하세요.
red_colors = rainbow[ 
0:3
  ]

#blue_colors가 ["파", "남", "보"]의 값을 가지도록 rainbow를 slice하세요.
blue_colors = rainbow[ 
-3:
 ]

print("red_colors의 값 : {}".format(red_colors))
print("blue_colors의 값 : {}".format(blue_colors))