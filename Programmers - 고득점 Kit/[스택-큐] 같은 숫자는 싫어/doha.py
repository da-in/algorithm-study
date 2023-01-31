def solution(arr):
    answer = []
    
    for i in arr:
        if answer and i == answer[-1]:
            continue
        else:
            answer.append(i)
    
    return answer