from collections import Counter
from itertools import combinations

def solution(weights):
#     t_weights=[[w*i for i in range(2,5)] for w in weights]
    
#     for i in range(len(t_weights)):
#         a,b,c,d = t_weights[i]
#         for j in range(i+1, len(t_weights)):
#             if i==j:
#                 continue
#             if a in t_weights[j] or b in t_weights[j] or c in t_weights[j] or d in t_weights[j]:
#                 answer+=1
    answer=0 
    weights.sort()
    cnt_weights=Counter(weights)
    comb_weights = list(combinations(cnt_weights.keys(),2))
    
    for k,v in cnt_weights.items():
        if v>1:
            answer+=v*(v-1)/2
    
    toque = [(4,3), (4,2), (3,2)]
    for w1,w2 in comb_weights:
        for t1,t2 in toque:
            if w1*t1==w2*t2:
                answer+=cnt_weights[w1]*cnt_weights[w2]
            
    return answer