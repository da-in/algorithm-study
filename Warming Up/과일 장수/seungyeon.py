def solution(k, m, score):
    answer = 0
    score = sorted(score)
    
    l = len(score)
    i = 1
    while(l >= m*i):
        answer += score[l-m*i]*m
        i+=1
    
    return answer