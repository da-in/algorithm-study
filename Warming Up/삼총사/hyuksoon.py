from bisect import bisect_left,bisect_right

def solution(number):
    answer = 0
    number.sort()
    
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            
            temp=0-(number[i]+number[j])
            
            l=bisect_left(number[j+1:],temp)
            r=bisect_right(number[j+1:],temp)
            
            answer+=r-l
    return answer
