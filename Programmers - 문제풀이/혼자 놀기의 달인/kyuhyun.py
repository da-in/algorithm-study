def solution(cards):
    res = []
    visit = [0] * (len(cards) + 1)

    for i in range(len(cards)) :
        count = 0
        cur = i + 1
        while visit[cur] == 0:
            count += 1
            visit[cur] = 1
            cur = cards[cur-1]
        if count != 0:
            res.append(count) 

    if len(res) == 1:
        return 0
    
    res.sort()
    answer = res[-1] * res[-2]

    return answer
