"""
문제 설명
1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

예를 들어

1	2	3	4
0	1	1	1
1	1	1	1
1	1	1	1
0	0	1	0
가 있다면 가장 큰 정사각형은

1	2	3	4
0	1	1	1
1	1	1	1
1	1	1	1
0	0	1	0
가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.
"""

def solution(board):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
    # print(len(board))
    # print(len(board[0]))
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] >= 1:
                board[i][j] += min(board[i-1][j-1], board[i][j-1], board[i-1][j])
                # print(board[i][j])
    # print(board)
    for i in board:
        if answer < max(i):
            answer = max(i)
            # print(answer)

    return answer * answer
