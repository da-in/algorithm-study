import math
def solution(brown, yellow):
    # 가로 + 세로
    total_brown = (brown + 4) // 2

    x = math.ceil(total_brown / 2)
    y = total_brown - x

    while y > 2:
        if (x-2) * (y-2) == yellow:
            return [x, y]
        else:
            x += 1
            y -= 1
