n = int(input())
grape = []
dp = [0] * n

for _ in range(n):
    val = int(input())
    grape.append(val)

dp[0] = grape[0]

for i in range(1, n):
    first = 0
    second = 0
    if i >= 2:
        first = grape[i] + dp[i-2]
    second = grape[i] + grape[i-1]
    if i >=3:
        second += dp[i-3]
    dp[i] = max(first, second, dp[i-1])

print(dp[n-1])
