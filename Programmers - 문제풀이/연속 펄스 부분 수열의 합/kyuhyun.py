def solution(sequence):
    plus_dp = [0] * (len(sequence) + 1)
    minus_dp = [0] * (len(sequence) + 1)

    plus_dp[1] = sequence[0]
    minus_dp[1] = -1 * sequence[0]

    for i in range(1, len(sequence)):

        plus_dp[i+1] = max(plus_dp[i] + sequence[i]*((-1)**i), sequence[i]*((-1)**i))
        minus_dp[i+1] = max(minus_dp[i] + sequence[i]*((-1)**(i+1)), sequence[i]*((-1)**(i+1)))

    return max(max(plus_dp), max(minus_dp))
