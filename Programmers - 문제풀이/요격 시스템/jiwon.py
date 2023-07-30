def solution(targets):
    answer = 0
    targets.sort(key = lambda x:x[1])
    
    system = 0
    for target in targets:
        if not target[0]<system<=target[1]:
            system = target[1]
            answer+=1
        
    return answer