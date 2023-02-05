def solution(n, times):

    left = min(times)
    rignt = max(times) * n
    mid = 0

    while left < rignt:
        mid = (left + rignt) // 2
        
        tmp = 0
        for time in times:
            tmp += mid // time

        if tmp >= n:
            rignt = mid
        else:
            left = mid + 1
            
    
    return left