def solution(N, number):
    
    dp = [[] for i in range(9)]
    
    if N == number:
        return 1
   
    for i in range(1, 9):
        dp[i].append(int(str(N) * i))

    for i in range(2, 9):
        for j in range(1, i):
            k = i - j
            for value1 in dp[j]:
                for value2 in dp[k]:
                    dp[i].append(value1 + value2)
                    dp[i].append(value1 * value2)
                    if value1 - value2 > 0:
                        dp[i].append(value1 - value2)
                    if value1 // value2 != 0:
                        dp[i].append(value1 // value2)
        dp[i] = set(dp[i])
        if number in dp[i]:
            return i
        
    return -1
