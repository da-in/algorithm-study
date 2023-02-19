def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left = 0
    right = distance

    while left <= right:
        mid = (left + right) // 2
        count = 0
        key = mid

        for rock in rocks:
            if key > rock:
                count += 1
            else:
                key = rock + mid
        if count >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer
