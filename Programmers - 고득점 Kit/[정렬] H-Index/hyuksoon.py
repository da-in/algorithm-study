def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    leng=len(citations)
    idx=0
    while idx<leng:
        if leng-idx>=citations[leng-idx-1]:
            answer=  citations[leng-idx-1]
        else:
            answer=max(answer,leng-idx)
        idx+=1
    return answer