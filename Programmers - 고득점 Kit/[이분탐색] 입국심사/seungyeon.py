def solution(n,times):
    
    times.sort()
    start=1
    end=times[len(times)-1]*n # 최대
    mid = 0

    # start,end,mid=1,times[len(times)-1]*n,0

    while start <= end:
        mid = (start+end)//2 # 최소 시간 후보

        person = 0
        for time in times:
            person += mid // time # 최소시간 후보 동안 상담 가능한 사람의 수
            
        if person < n:
            start = mid + 1
        else:
            end = mid - 1

    return start 