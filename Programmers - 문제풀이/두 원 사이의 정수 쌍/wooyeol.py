"""
    두 원 사이의 정수 쌍
    https://school.programmers.co.kr/learn/courses/30/lessons/181187
    

    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 단순 구현
    
     
    1. r2에 포함되는 정수 좌표 - r1에 포함되는 정수 좌표
    (r2 원의 내접사각형 + r2의 x축과 y축에 접하는 점 4개) - (r1 원의 내접 사각형)
    # 5**2 - 3**2 + 4
    # (r2지름 - 1)^2 - (r1지름 - 1)^2 + 4
    1) r1 < r2
    2) r1 >= 1

    2. 피타고라스를 사용하여 직접 구해보자
    풀이참조 : https://school.programmers.co.kr/questions/47373
    x^2 + y^2 = r^2
    r^2 - x^2 = y^2
    y = sqrt(r^2 - x^2)

"""
from math import floor, ceil, sqrt


def solution(r1, r2):
    answer = 0
    min_y, max_y = r1, r2

    # 제1 사분면의 정수 쌍의 갯수를 구하고 4배하기
    ## x값을 고정하고 y 값을 찾으며 연산

    # 0부터 시작하였을 때는 4배를 하는 순간 중복된 점을 포함하기 때문에 제외하고 1부터 x 탐색
    for x in range(1, r2 + 1):
        # 최대 y 값의 범위는 버림 연산을 통해 구한다.
        max_y = floor(sqrt(r2**2 - x**2))  # 버림

        # 최소 y 값의 범위는 r1보다 커야하기에 올림 연산을 통해 구한다.
        min_y = 0 if x > r1 else ceil(sqrt(r1**2 - x**2))  # 올림
        answer += max_y - min_y + 1  # max_y ~ min_y 범위의 점의 갯수는 max_y-min_y+1

    return answer * 4  # 총 4사분면 전체에 대한 갯수


# 1 Case #1
r1, r2 = 2, 3
print(solution(r1, r2))

# 테스트 1 〉	통과 (0.02ms, 10MB)
# 테스트 2 〉	통과 (0.04ms, 10.1MB)
# 테스트 3 〉	통과 (0.05ms, 10.1MB)
# 테스트 4 〉	통과 (1.14ms, 10.2MB)
# 테스트 5 〉	통과 (1.19ms, 10.2MB)
# 테스트 6 〉	통과 (2.54ms, 9.94MB)
# 테스트 7 〉	통과 (623.90ms, 10.1MB)
# 테스트 8 〉	통과 (957.51ms, 10.1MB)
# 테스트 9 〉	통과 (540.68ms, 10MB)
# 테스트 10 〉	통과 (877.39ms, 10.2MB)
