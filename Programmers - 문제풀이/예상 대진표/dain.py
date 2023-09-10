import math

def solution(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
    return answer
