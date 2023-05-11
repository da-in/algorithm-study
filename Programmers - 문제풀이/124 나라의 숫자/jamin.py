def solution(n):
    answer = ''
    nums = ['1','2','4']
    mod = 0
    
    while n>0:
        mod = (n-1)%3
        answer += nums[mod]
        n = (n-1)//3
    
    return answer[::-1]