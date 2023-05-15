def solution(cards):
    visit=[False for i in range(len(cards))]
    data=[]
    for i in range(len(cards)):
        if not visit[i]:
            target=cards[i]-1
            count=1
            visit[i]=True
            while not visit[target]:
                visit[target]=True
                count+=1
                target=cards[target]-1
            data.append(count)
    data.sort(reverse=True)
    if len(data)>1:
        return data[0]*data[1]
    return 0