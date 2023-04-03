def solution(n):
    dp = [[1] for _ in range(n+1)]
    dp[2] = 3
    sum = 0
    
    if n % 2 == 1 :
        return 0
    else:
        for i in range(4, n+1, 2):
            sum += dp[i-4] * 2
            dp[i] = (dp[2] * dp[i - 2] + sum) % 1000000007 
    return dp[n]
