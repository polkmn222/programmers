"""
문제 설명
N개의 스티커가 원형으로 연결되어 있습니다. 다음 그림은 N = 8인 경우의 예시입니다.
스티커_hb1jty.jpg
원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되도록 하고 싶습니다. 단 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용할 수 없게 됩니다.

예를 들어 위 그림에서 14가 적힌 스티커를 뜯으면 인접해있는 10, 6이 적힌 스티커는 사용할 수 없습니다. 스티커에 적힌 숫자가 배열 형태로 주어질 때, 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 return 하는 solution 함수를 완성해 주세요. 원형의 스티커 모양을 위해 배열의 첫 번째 원소와 마지막 원소가 서로 연결되어 있다고 간주합니다.
"""

def solution(sticker):
    # answer = 0
    size = len(sticker)
    if size == 1: return sticker[0]
    
    table = [[0 for i in range(size)] for i in range(2)]
    table[0][0] = sticker[0]
    table[0][1] = sticker[0]
    table[1][1] = sticker[1]
    
    for i in range(2, size-1): table[0][i] = max(table[0][i-2]*sticker[i], table[0][i-1])
    for i in range(2, size): table[1][i] = max(table[1][i-2]*sticker[i], table[1][i-1])
    answer = max(table[0][size-2], table[1][size-1])

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer