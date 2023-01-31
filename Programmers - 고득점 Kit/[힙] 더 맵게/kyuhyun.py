from heapq import *

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)

    while 1:
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            return -1

        newFood = heappop(scoville) + heappop(scoville) * 2
        heappush(scoville, newFood)
        answer += 1

    return answer
