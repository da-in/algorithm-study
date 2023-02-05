def triple(st):
    return st*3

def solution(numbers):
    answer = ''
    
    if sum(numbers) == 0:
        return '0'
    
    numbers = list(map(str, numbers))
    numbers.sort(key = triple, reverse=True)
    
    
    answer = str(''.join(numbers))
    
    return answer
