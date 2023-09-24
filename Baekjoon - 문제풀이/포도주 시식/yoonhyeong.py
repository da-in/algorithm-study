
N = int(input())

wine = [0]

for i in range(N):
    wine.append(int(input()))

dp = [0] * (N+1)

dp[1] = wine[1]

if N > 1:
    dp[2] = wine[1] + wine[2]


for i in range(3, N+1):
    dp[i] = max(dp[i-2] + wine[i], dp[i-1], dp[i-3] + wine[i-1] + wine[i])  # 1. 현재 잔과 전전 잔을 마실때, 2. 현재잔을 마시지 않을 때, 3. 현재 잔과 이전 잔을 마시고 전전 잔을 마시지 않을 때

print(dp[N])

