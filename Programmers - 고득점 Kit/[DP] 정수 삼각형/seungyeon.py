def main():
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

def solution(triangle):
    answer = 0
    n = len(triangle)

    dp = [[0 for j in range(n)] for i in range(n)]

    dp[0][0] = triangle[0][0]

    for i in range(n):
        for j in range(i):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]

            answer = max(answer,dp[i][j])
    return answer

if __name__ == "__main__":
    main()