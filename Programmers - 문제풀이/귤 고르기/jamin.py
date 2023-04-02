from collections import Counter

def solution(k, tangerine):
    total = 0
    dic = Counter(tangerine)
    
    val = list(dic.values())
    val.sort(reverse=True)
    
    for i,j in enumerate(val):
        total += val[i]
        if total >= k:
            break
    
    
    return i+1

# def solution(k, tangerine):
#     dic = {}
    
#     for i in range(len(tangerine)):
#         if tangerine[i] in dic:
#             dic[tangerine[i]] +=1
            
#             if dic[tangerine[i]]>=k:
#                 return 1
#         else:
#             dic[tangerine[i]] = 1

#     val = list(dic.values())
#     val.sort(reverse=True)
    
#     total = 0
#     for i,j in enumerate(val):
#         total += val[i]
#         if total >= k:
#             break
    
    
#     return i+1