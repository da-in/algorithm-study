from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    data=defaultdict(int)
    for t in tangerine:
        data[t]+=1
    sorted_dict = sorted(data.items(), key = lambda item: -item[1])
    for s in sorted_dict:
        k-=s[1]
        answer+=1
        if k<=0:
            break
    return answer
