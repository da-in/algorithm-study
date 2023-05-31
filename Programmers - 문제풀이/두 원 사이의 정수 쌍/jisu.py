"""
# 16:20 -> 13:32 (?)
- 첫 번째 접근 : 완전탐색 (시간 초과)
- 두 번째 접근 
    - 1사분면 기준 축(axis) 위 점들 제외, 원 사이의 공간에 있는 점들의 개수를 구하기
        - 원 내부 공간의 점 개수를 구하는 get_num_of_points_in_circle 활용
        - get_num_of_points_in_circle(r2) - get_num_of_points_in_circle(r1) 하면 두 원 사이 공간의 점들의 개수를 구할 있다.
        - 하지만 예외를 고려해야하는디...
            - 두 번째 원 내부 점의 개수를 첫 번째 원 내부 점 개수에서 뺄 때 두 번째 원 위의 점까지 같이 빼지는 이슈
            - flog 인자를 두어서 두 번째 원 내부 점 개수를 구할 때만 예외처리
        - 1사분면 기준으로 원 사이 공간 점들의 개수를 구했으므로 * 4를 해주어 전채 원 사이 공간 점의 개수를 얻는다.
    - 축 위의 점들을 제외했으므로 축 위의 점들을 추가로 고려해주기
        - num_of_points_on_axis
"""

from math import sqrt

flag = False # 두 번째 원 위 점 예외처리를 위한 flag 변수


def get_num_of_points_in_circle(r):
    """
    축 위의 점들을 제외한 원 내부(1사분면 기준)의 점 개수 구하기

    x^2 = r^2 - y^2 임을 활용하여 y를 순회하며 해당 y의 x축 점들의 개수를 세어 합산
    r1에 대한 개수를 구할 때 점이 원 위에 위치한다면 추후 뺄셈 과정(46번째 라인)에서 함께 제외되므로 예외처리(36번째 라인)
    """
    global flag

    num_of_points = 0

    for y in range(1, r):
        x_square = r**2 - y**2

        if flag and int(sqrt(x_square)) == sqrt(x_square): # 두 번째 원 위 점 예외처리
            num_of_points += int(sqrt(x_square))-1 
        else:
            num_of_points += int(sqrt(x_square))            # 해당 y의 x축 점 개수를 세어 합산
    
    flag = True     

    return int(num_of_points)

def solution(r1, r2):
    num_of_points_in_circle = (get_num_of_points_in_circle(r2) - get_num_of_points_in_circle(r1)) * 4   # 원 사이 공간 점들의 개수
    num_of_points_on_axis = (r2-r1+1) * 4   # 축 위의 점 개수
    return num_of_points_in_circle + num_of_points_on_axis

case1 = [2, 3]          # 20
case2 = [2, 4]          # 40
case3 = [1, 2]          # 12
case4 = [1, 3]          # 28
print(solution(*case1))
print(solution(*case2))
print(solution(*case3)) 
print(solution(*case4)) 