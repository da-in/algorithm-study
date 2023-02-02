from itertools import permutations
import math


def solution(numbers):

    answer = 0
    lists = []
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        temp = list(permutations(numbers, i))
        for i in temp:
            lists.append(int(''.join(i)))
    lists = list(set(lists))
    for i in lists:
        temp = True
        if i < 2:
            continue
        else:
            for l in range(2, int(math.sqrt(i))+1):
                if i % l == 0:
                    temp = False
        if temp:
            answer += 1

    return answer

def solution(numbers):
    answer = 0
    data={}
    def ck(x):
        if x==0 or x==1:
            return False
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
        return True
    for i in range(1, len(numbers)+1):
        temp = list(permutations(numbers, i))
        for i in temp:
            num=int(''.join(i))
            if num not in data:
                data[num]=1
                if ck(num):
                    answer+=1
    return answer