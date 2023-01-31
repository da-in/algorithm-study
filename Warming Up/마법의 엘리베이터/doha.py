def solution(storey):
    answer = 0
    
    while storey:
        tmp = storey % 10
        
        if tmp <= 4:
            answer += tmp
            storey = storey // 10
            
        elif tmp == 5 and storey // 10 % 10 < 5:
            answer += tmp
            storey = storey // 10
            
        else:
            answer += 10 - tmp
            storey += 10 - tmp
            storey = storey // 10
            
    return answer