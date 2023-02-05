from itertools import *


def isDecimal(num):

    if num == 0 or num == 1:
        return False

    for i in range(2, num//2+1):
        if num % i == 0:    
            return False
    return True

def solution(numbers):
    visit = [0] * 10000000
    answer = 0
    
    for i in range(len(numbers)):
        num_str = list(map("".join, permutations(list(numbers), i+1)))
        num_int = list(map(int, num_str))

        for j in range(len(num_int)):
            if not visit[num_int[j]] and isDecimal(num_int[j]):
                visit[num_int[j]] = True
                answer += 1

    return answer
