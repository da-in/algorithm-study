def solution(n, times):
    answer = min(times)*n
    
    def calc(x):
        num=0
        for t in times:
            num+=x//t
        return num
    l=1
    r=answer
    while l<=r:
        mid=(l+r)//2
        if calc(mid)>=n:
            r=mid-1
            answer=min(answer,mid)
        else:
            l=mid+1
    return answer
