def solution(x, y, n):

    dp = [set() for _ in range(20)]
    dp[0].add(x)
    
    if x == y :
        return 0

    for i in range(1, len(dp)):
        for val in dp[i-1]:
            dp[i].add(val + n)
            dp[i].add(val * 2)
            dp[i].add(val * 3)
        if y in dp[i]:
            return i
    return -1
