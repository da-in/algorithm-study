def solution(prices):
    answer = []
    for i in range(len(prices)):
        k = True
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                k = False
                break
        if k:
            answer.append(len(prices)-i-1)
    return answer