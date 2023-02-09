def solution(phone_book):
    answer = True
    result = {}
    
    for p in phone_book:
        for i in range(1, len(p)):
            result[p[0:i]] = 0
            
    for p in phone_book:
        if p in result:
            return False
        
    return answer