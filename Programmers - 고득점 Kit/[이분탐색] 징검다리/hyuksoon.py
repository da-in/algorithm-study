def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    l=0
    r=distance
    
    while l<=r:
        mid=(l+r)//2
        cnt=0
        idx=0
        ck=True
        for i in rocks:
            if i-idx<mid:
                if cnt<n:
                    cnt+=1
                else:
                    ck=False
                    break
            else:
                idx=i
        if ck:
            answer=max(mid,answer)
            l=mid+1
        else:
            r=mid-1
    
    
    return answer