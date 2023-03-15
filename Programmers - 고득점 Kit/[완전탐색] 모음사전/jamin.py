from itertools import product

def solution(word):
    dic = []
    for i in range(1,6): 
        for j in product(['A','E','I','O','U'],repeat=i):   #a,e,i,o,u,(a,a),(a,e)...
            dic.append("".join(j))
    dic.sort()
    return dic.index(word)+1