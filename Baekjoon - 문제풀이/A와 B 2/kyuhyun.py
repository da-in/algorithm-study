S = input()
T = input()

dp = [[] for _ in range((len(T) + 1))]
dp[len(T)].append(T)

for i in range(len(T)-1, len(S)-1, -1):
    for val in dp[i+1]:
        if val[-1] == 'A':
            dp[i].append(val[:-1])
        if val[::-1][-1] == 'B':
            dp[i].append(val[::-1][:-1])
    dp[i] = set(dp[i])

if S in dp[len(S)]:
    print(1)
else:
    print(0)
