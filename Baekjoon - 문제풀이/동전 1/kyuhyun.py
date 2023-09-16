n, k = map(int, input().split(" "))

coins = []
dp = [0] * (k+1)
dp[0] = 1

for _ in range(n):
    num = int(input())
    coins.append(num)

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i - coin]

print(dp[k])
