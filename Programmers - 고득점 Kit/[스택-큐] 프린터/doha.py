def solution(priorities, location):
    answer = 1
    
    ready = {}
    for i, p in enumerate(priorities):
        ready[i] = p
        
    while list(ready.keys())[0] != location or ready[list(ready.keys())[0]] != max(list(ready.values())):
        if ready[list(ready.keys())[0]] == max(list(ready.values())):
            ready.pop(list(ready.keys())[0])
            answer += 1
        else:
            index = list(ready.keys())[0]
            tmp = ready.pop(list(ready.keys())[0])
            ready[index] = tmp
    
    return answer