from heapq import heappush, heappop,heapify
def solution(n, works):
    answer = 0
    heapify(works)
    h=[]
    for w in works:
        heappush(h,-w)
    for i in range(n):
        while h and -h[0]>0:
            temp=-heappop(h)
            if temp>0:
                temp-=1
                heappush(h,-temp)
                break
        
    for i in h:
        answer+=(-i)**2
    return answer