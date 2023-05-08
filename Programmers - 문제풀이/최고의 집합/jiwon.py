def solution(n, s):
    if s<n:
        return [-1]
    
    answer = []
    
    rest = s-(s//n)*n
    for _ in range(n):
        if rest:
            answer.append(s//n+1)
            rest-=1
        else:
            answer.append(s//n)
    
    return sorted(answer)