def solution(money):
    answer = 0
    dp=[[0,0,0]for i in range(len(money))]
    dp[0][0]=0
    dp[0][1]=0
    dp[0][2]=0
    
    
    for i in range(1,len(money)):
        dp[i][0]=max(dp[i-1][1],dp[i-1][2])+money[i]
        dp[i][1]=dp[i-1][0]
        dp[i][2]=dp[i-1][1]
    answer=max(dp[-1])
        
    
    #끊어져 있을 때의 코드
    dp=[[0,0,0]for i in range(len(money))]
    dp[0][0]=money[0]
    dp[0][1]=0
    dp[0][2]=0
    
    for i in range(1,len(money)):
        dp[i][0]=max(dp[i-1][1],dp[i-1][2])+money[i]
        dp[i][1]=dp[i-1][0]
        dp[i][2]=dp[i-1][1]
    #answer=max(dp[-1])
    answer=max(dp[-1][1],dp[-1][2],answer)
    
    return answer






