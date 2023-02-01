import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville and scoville[0] < K:
            try:
                result1 = heapq.heappop(scoville)
                result2 = heapq.heappop(scoville)
                heapq.heappush(scoville, result1+(2*result2))
                answer += 1
            except:
                heapq.heappush(scoville, result1)
                break
    if scoville[0] >= K:
            return answer
    else:
            return -1