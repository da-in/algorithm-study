def solution(clothes):
    answer=1
    closet = {}
    for name, case in clothes:
        if case in closet:
            closet[case]+=1
        else:
            closet[case]=1
    
    closet = closet.values()
    
    for c in closet:
        answer*=(c+1)
    
    return answer-1