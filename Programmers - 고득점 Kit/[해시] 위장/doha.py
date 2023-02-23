def solution(clothes):
    answer = 1
    mix = {}
    
    for cloth in clothes:
        if cloth[1] in mix:
            mix[cloth[1]].append(cloth[0])
        else:
            mix[cloth[1]] = [cloth[0]]
            
    len_mix = [] 
    for m in mix:
        len_mix.append(len(mix[m])+1) 

    for l in len_mix: 
        answer *= l
        
    return answer - 1