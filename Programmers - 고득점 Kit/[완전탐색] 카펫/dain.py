import math

def solution(brown, yellow):
    answer = []
    for yh in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % yh == 0:
            yw = yellow // yh
            if 4 + 2 * (yh + yw) == brown:
                answer = [yw + 2, yh + 2]
    return answer
