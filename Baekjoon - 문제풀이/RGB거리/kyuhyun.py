N = int(input())

cost = [[0]]
for i in range(N):
    val = list(map(int, input().split(" ")))
    cost.append(val)

dp = [[0 for _ in range(3)] for _ in range(N+1)]
dp[1] = cost[1]

for i in range(2, N+1):
    dp[i][0] = min(dp[i-1][1] + cost[i][0], dp[i-1][2] + cost[i][0])
    dp[i][1] = min(dp[i-1][0] + cost[i][1], dp[i-1][2] + cost[i][1])
    dp[i][2] = min(dp[i-1][0] + cost[i][2], dp[i-1][1] + cost[i][2])
    print(dp)

print(min(dp[N]))
