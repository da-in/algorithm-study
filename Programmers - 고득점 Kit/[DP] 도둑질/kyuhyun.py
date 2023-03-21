def solution(money):
    l = len(money)

    if l < 4:
        return max(money)

    dp_start = [0]
    dp_end = [0]

    for i in range(1, l):
        dp_end.append(money[i])

    for i in range(l - 1):
        dp_start.append(money[i])

    
    for i in range(2, l) :
        dp_start[i] = max(dp_start[i-1], dp_start[i-2] + dp_start[i])    
        dp_end[i] = max(dp_end[i-1], dp_end[i-2] + dp_end[i])

    return max(dp_start[l-1], dp_end[l-1])     
    
