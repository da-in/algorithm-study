import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1

for coin in coins:
    for i in range(coin, len(dp)):
        dp[i] = dp[i] + dp[i-coin]

print(dp[k])