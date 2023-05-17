def solution(cards):
    answer = []
    visited=[0 for _ in range(len(cards))]
    
    for idx, card in enumerate(cards):
        box_num=0
        while 0 in visited:
            if visited[card-1]==0:
                visited[card-1]=1
                box_num+=1
                card = cards[card-1]
            else:
                break
        if box_num!=0:
            answer.append(box_num)
            
    answer.sort()
    
    return answer[-1]*answer[-2] if len(answer)>1 else 0