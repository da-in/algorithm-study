
N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))

coins.sort()

DP = [0] * (K + 1)
DP[0] = 1

for i in coins:
    for j in range(i, K+1):
        DP[j] += DP[j-i]

print(DP[K])

