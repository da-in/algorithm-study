def solution(arr):
    answer = []
    
    answer.append(arr[0])

    for i in range(len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
            
    return answer
