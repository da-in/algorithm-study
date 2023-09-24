import sys

n = int(sys.stdin.readline())
grapes = [int(sys.stdin.readline()) for _ in range(n)]

result = 0
dp = [0 for _ in range(len(grapes)+1)]
dp[1] = grapes[0]
dp[2] = grapes[1]

for i in range(2, len(dp)):
    dp[i] = max(grapes[i-2], grapes[i-1]+grapes[i-2])

print(result) 