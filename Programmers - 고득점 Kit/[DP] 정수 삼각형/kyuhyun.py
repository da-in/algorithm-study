def solution(triangle):

    dp = [[] for i in range(len(triangle))]
    dp[0] = triangle[0]

    for i in range(1, len(triangle)):
        dp[i].append(dp[i-1][0] + triangle[i][0])
        for j in range(len(dp[i-1])-1):
            dp[i].append(max(dp[i-1][j] + triangle[i][j+1], dp[i-1][j+1] + triangle[i][j+1]))
        dp[i].append(dp[i-1][-1] + triangle[i][-1])

    return max(dp[-1])
