"""
문제 설명
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

U: 위쪽으로 한 칸 가기

D: 아래쪽으로 한 칸 가기

R: 오른쪽으로 한 칸 가기

L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.

방문길이1_qpp9l3.png

예를 들어, "ULURRDLLU"로 명령했다면

방문길이2_lezmdo.png

1번 명령어부터 7번 명령어까지 다음과 같이 움직입니다.
방문길이3_sootjd.png

8번 명령어부터 9번 명령어까지 다음과 같이 움직입니다.
방문길이4_hlpiej.png

이때, 우리는 게임 캐릭터가 지나간 길 중 캐릭터가 처음 걸어본 길의 길이를 구하려고 합니다. 예를 들어 위의 예시에서 게임 캐릭터가 움직인 길이는 9이지만, 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다. (8, 9번 명령어에서 움직인 길은 2, 3번 명령어에서 이미 거쳐 간 길입니다)

단, 좌표평면의 경계를 넘어가는 명령어는 무시합니다.

예를 들어, "LULLLLLLU"로 명령했다면

방문길이5_nitjwj.png

1번 명령어부터 6번 명령어대로 움직인 후, 7, 8번 명령어는 무시합니다. 다시 9번 명령어대로 움직입니다.
방문길이6_nzhumd.png

이때 캐릭터가 처음 걸어본 길의 길이는 7이 됩니다.

명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.
"""

def solution(dirs):
    answer = 0
    a = set()
    b = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x , y = 0, 0
    for i in dirs:
        nx, ny = x + b[i][0], y + b[i][1]
        # print(b[i][0])
        # print('nx', nx)
        # print('ny', ny)
        if (-5 <= nx <= 5) and (-5 <= ny <= 5):
            a.add((x, y, nx, ny))
            a.add((nx, ny, x, y))
            x, y = nx, ny
    answer = len(a) // 2        
    return answer

# def solution(dirs):
#     answer = 0
#     a = set()
#     x = 0
#     y = 0
#     for i in dirs:
#         if i == 'U' and y < 5:
#             a.add(((x, y), (x, y+1)))
#             y += 1
#         elif i == 'D' and y > -5:
#             a.add(((x, y-1), (x, y)))
#             y -= 1
#         elif i == 'R' and x < 5:
#             a.add(((x, y), (x+1, y)))
#             x += 1
#         elif i == 'L' and x > -5:
#             a.add(((x-1, y), (x, y)))
#             x -= 1
#     answer = len(a)        
#     return answer
