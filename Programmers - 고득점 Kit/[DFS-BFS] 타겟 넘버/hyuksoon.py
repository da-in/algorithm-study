def solution(numbers, target):
    global answer
    answer = 0
    def calc(x,n):
        global answer
        if n<len(numbers):
            calc(x+numbers[n],n+1)
            calc(x-numbers[n],n+1)
        else:
            if x==target:
                answer+=1
        
    calc(0,0)
            
        
    return answer