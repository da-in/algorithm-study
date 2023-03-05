from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while(scoville[0] < K):
        a = heappop(scoville)
        b = heappop(scoville)
        heappush(scoville, a+b*2)
        answer+=1
        if(len(scoville)==1 and scoville[0]<K):
            answer = -1
            break
        
    return answer