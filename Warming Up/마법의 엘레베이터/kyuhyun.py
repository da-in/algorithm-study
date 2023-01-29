def solution(storey):
    
    answer = 0
    while (storey):
        button = storey % 10
        
        if button > 5:
            answer += (10 - button)
            storey += 10
        elif button < 5:
            answer += button
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += 5
        storey //= 10
         
    return answer
