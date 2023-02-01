from itertools import permutations

def solution(numbers):
    answer = []                                   
    num = [n for n in numbers]                   
    permutate = []  
    
    for i in range(1, len(numbers)+1):            
        permutate += list(permutations(num, i))        
    result_num = [int(('').join(p)) for p in permutate]   

    for r in result_num:                            
        if r < 2:                                 
            continue

        is_prime = True

        for i in range(2,int(r**0.5) + 1):        
            if r % i == 0:                        
                is_prime = False
                break
            
        if is_prime:
            answer.append(r)                      

    return len(set(answer))      