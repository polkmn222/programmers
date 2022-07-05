"""
문제 설명
문자열 s와 자연수 n이 입력으로 주어집니다. 문자열 s를 좌측 / 가운데 / 우측 정렬한 길이 n인 문자열을 한 줄씩 프린트해보세요.
"""

s, n = input().strip().split(' ')
n = int(n)
# print(s+" "*n+"\n"+
#      " "*int(n/2) + s + " "* int(n/2)+"\n"+
#      " "*n+s)
# # print(" "*int(n/2) + s + " "* int(n/2))
# # print(" "*n+s)
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))