def solution(answers):
    answer = []
    n = len(answer)
    
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    result = [0, 0, 0]
    
    for i, a in enumerate(answers):
        if a == arr1[i % 5]:
            result[0] += 1
        if a == arr2[i % 8]:
            result[1] += 1
        if a == arr3[i % 10]:
            result[2] += 1
    
    max_num = max(result)
    for i, r in enumerate(result):
        if r == max_num:
            answer.append(i+1)
    return answer