def solution(scores):
    answer=1
    wonho = [scores[0][0],scores[0][1]]
    scores.sort(key=lambda s: (-s[0], s[1]))
    temp=0
    
    for score in scores:
        
        if wonho[0] < score[0] and wonho[1] < score[1]:
            return -1
        
        if temp <= score[1]:
            if sum(wonho) < score[0] + score[1]:
                answer += 1
            temp = score[1]
            
    return answer