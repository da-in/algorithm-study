from itertools import *
def solution(k, dungeons):
    max = 0
    result = list(permutations(dungeons, len(dungeons)))
    
    for cal in result:
        sub_k = k
        answer = 0
        for st, ed in cal:
            if sub_k >= st:
                sub_k -= ed
                answer += 1
            else:
                break
        if max < answer:
            max = answer

    return max
