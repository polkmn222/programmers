"""
문제 설명
길이가 n인 배열에 1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는지를 확인하려고 합니다.
1부터 n까지 숫자가 중복 없이 한 번씩 들어 있는 경우 true를, 아닌 경우 false를 반환하도록 함수 solution을 완성해주세요.
"""

def solution(arr):
    answer = True

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')
    arr.sort()
    if len(arr) != arr[-1]:
        answer = False
    
    

    return answer