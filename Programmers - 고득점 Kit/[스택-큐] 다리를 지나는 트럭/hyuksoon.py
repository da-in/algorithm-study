from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights=truck_weights[::-1]
    q=deque()
    
    restW=weight
    while truck_weights:
        answer+=1
        if q and answer-q[-1][1]>=bridge_length:
            restW+=q.pop()[0]
        target=truck_weights.pop()
        if target<=restW:
            q.appendleft([target,answer])
            restW-=target
        else:
            while target>restW:
                temp=q.pop()
                restW+=temp[0]
                answer+=bridge_length- (answer-temp[1])
            q.appendleft([target,answer])
            restW-=target
                
    

    return answer+bridge_length
