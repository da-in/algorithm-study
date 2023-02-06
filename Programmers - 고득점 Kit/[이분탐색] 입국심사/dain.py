from functools import reduce

def solution(n, times):
    times.sort()
    left = 0
    right = answer = times[-1] * n
    mid = (left + right) // 2
    while left <= right:
        cnt = reduce(lambda acc, cur: acc + mid // cur, times, 0)
        if cnt >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return answer
