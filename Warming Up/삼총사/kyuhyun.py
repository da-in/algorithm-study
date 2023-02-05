def solution(number):
    answer = 0
    
    for i in range(0, len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                if(number[i]+number[j]+number[k] == 0):
                    answer += 1  
                    
    return answer
