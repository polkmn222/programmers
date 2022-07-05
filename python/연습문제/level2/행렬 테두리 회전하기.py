"""
문제 설명
rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다. 이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다. 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.

x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.
다음은 6 x 6 크기 행렬의 예시입니다.

grid_example.png

이 행렬에 (2, 2, 5, 4) 회전을 적용하면, 아래 그림과 같이 2행 2열부터 5행 4열까지 영역의 테두리가 시계방향으로 회전합니다. 이때, 중앙의 15와 21이 있는 영역은 회전하지 않는 것을 주의하세요.

rotation_example.png

행렬의 세로 길이(행 개수) rows, 가로 길이(열 개수) columns, 그리고 회전들의 목록 queries가 주어질 때, 각 회전들을 배열에 적용한 뒤, 그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
"""

def solution(rows, columns, queries):
    matrix = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]
    answer = []
    
    for t, l, b, r in queries:
        top, left, bottom, right = t-1, l-1, b-1, r-1
        tmp = matrix[top][left]
        minimum = tmp

        for y in range(top, bottom):
            value = matrix[y+1][left]
            matrix[y][left] = value
            minimum = min(minimum, value)
            
        for x in range(left, right):
            value = matrix[bottom][x+1]
            matrix[bottom][x] = value
            minimum = min(minimum, value)
            
        for y in range(bottom, top, -1):
            value = matrix[y-1][right]
            matrix[y][right] = value
            minimum = min(minimum, value)
            
        for x in range(right, left, -1):
            value = matrix[top][x-1]
            matrix[top][x] = value
            minimum = min(minimum, value)
        
        matrix[top][left+1] = tmp
        answer.append(minimum)
        
    return answer