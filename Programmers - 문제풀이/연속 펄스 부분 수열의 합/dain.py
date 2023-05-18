def dp(s):
    dp = [0] * len(s)
    for i in range(len(s)):
        dp[i] = max(s[i], s[i] + dp[i - 1])
    return max(dp)

def solution(sequence):
    answer = 0
    s1 = list(map(lambda s: s[1] * (1 if s[0] % 2 == 0 else -1), enumerate(sequence)))
    s2 = list(map(lambda s: s[1] * (-1 if s[0] % 2 == 0 else 1), enumerate(sequence)))
    return max(dp(s1), dp(s2))
