from collections import Counter

def solution(k, tangerine):
    t_num = sorted(list(Counter(tangerine).values()))[::-1]
    i=0
    while k>0:
        k-=t_num[i]
        i+=1
    
    return i