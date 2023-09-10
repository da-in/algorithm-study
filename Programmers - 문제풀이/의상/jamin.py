def solution(clothes):
    answer = 1
    clo = {}
    val = []
    
    for i in range(len(clothes)):
        if clothes[i][1] not in clo:
            clo[clothes[i][1]] = 1
        else:
            clo[clothes[i][1]] += 1
            
    val = list(clo.values())
    
    for j in val:
        answer *= (j+1)
        
    return answer-1