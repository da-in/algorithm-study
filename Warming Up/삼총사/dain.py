import itertools

def solution(number):
    answer = 0
    C = itertools.combinations(number, 3)
    for c in C:
        if sum(c) == 0:
            answer += 1
    return answer
