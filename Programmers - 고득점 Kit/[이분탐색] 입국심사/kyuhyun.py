def solution(n, times):
    answer = 0
    times = sorted(times)

    left = times[0]
    right = times[0] * n

    while left <= right:
        count = 0
        mid = (left + right) // 2

        for i in times:
            count += (mid // i)
        if count >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer
