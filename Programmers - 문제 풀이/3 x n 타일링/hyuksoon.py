def solution(n):
    num=4
    dp=[1,3,11]
    if n%2==1:
        return 0
    if n==2:
        return 3
    if n==4:
        return 11
    while True:
        num+=2
        temp=0
        for d in dp[:-1]:
            temp+=d*2
        temp+=dp[-1]*3
        temp%=1000000007
        dp.append(temp)
        if n==num:
            return temp