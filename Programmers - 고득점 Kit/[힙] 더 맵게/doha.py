import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    for i in range(len(scoville)-1):
        if scoville[0] < K:
            low1 = heapq.heappop(scoville)
            low2 = heapq.heappop(scoville) * 2
            heapq.heappush(scoville, low1 + low2)
            answer += 1
        else:
            break
    if scoville[0] < K:
        return -1
    return answer