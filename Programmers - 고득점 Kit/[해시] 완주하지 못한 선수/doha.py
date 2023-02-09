def solution(participant, completion):
    comp_dict = {}
    for c in completion:
        if c in comp_dict:
            comp_dict[c] += 1
        else:
            comp_dict[c] = 1
    
    for p in participant:
        if p in comp_dict:
            if(comp_dict[p] == 0):
                return p
            comp_dict[p] -= 1
            
        else:
            return p