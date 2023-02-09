def solution(citations):
    citations.sort()
    max = l = len(citations)
    
    for idx, num in enumerate(citations):
        if num == l - idx:
            return num
        elif num < l - idx:
            max = (l - idx) -1
            
    return max
