def solution(number, k):
    answer = ''
    max = number[0]

    # 차례대로 answer에 더하고 max보다 큰 수가 나온다면 answer[-1] < max 인 수 빼기 
    for num in number:
        if max < num:
            max = num
            while answer and answer[-1] < max and k > 0:
                answer = answer[:-1]
                k -= 1
        max = num
        answer += num
        
    if k != 0:
        return answer[:(len(answer) - k)]
    
    return answer
