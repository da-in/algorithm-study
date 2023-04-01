def solution(k, tangerine):
    answer = 0
    kind = {}

    for val in tangerine:
        if val in kind.keys():
            kind[val] +=  1
        else:    
            kind[val] = 1

    kind = sorted(kind.items(), key=lambda x : x[1])
    
    while k > 0:
        _, val = kind.pop()
        k -= val
        answer += 1
        
    return answer
