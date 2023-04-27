def solution(scores):
    answer=1
    wanho = scores[0]
    wanho_sum = sum(wanho)
    
    scores = sorted(scores, key=lambda x:(-x[0],x[1]))
    x = scores[0][1]
    
    for score in scores:
        if score[0]>wanho[0] and score[1]>wanho[1]:
            return -1
        if score[1]>=x:
            x=score[1]
            if sum(score)>wanho_sum:
                answer+=1
    
    return answer