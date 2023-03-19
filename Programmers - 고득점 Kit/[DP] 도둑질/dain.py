def solution(money):
    l = len(money)
    dp = [0] * l
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, l - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

    dp2 = [0] * l
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, l):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    return max(dp[l - 2], dp2[l - 1])
