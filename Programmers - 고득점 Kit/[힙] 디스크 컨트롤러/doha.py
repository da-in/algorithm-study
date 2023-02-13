import heapq

def solution(jobs):
    time, start, end, now, disk = 0, 0, 0, 0, 0
    disk, heap, wait= [], [], []
    heapq.heapify(wait)

    for j in jobs:
        heapq.heappush(heap,j)

    job = len(heap)

    while True:
        for t in range(len(heap)):
            if time >= heap[0][0]:
                heapq.heappush(wait, heapq.heappop(heap))

        wait.sort(key = lambda x : x[-1])
        
        if len(disk) == 0:
            if len(wait) != 0:
                disk = heapq.heappop(wait)
                start = time 
                end = time + disk[1]
        else:
            if time == end :
                now += end - disk[0]
                disk = []                
                continue

        time += 1 

        if len(heap) == 0 and len(disk) == 0:
            break

    return now // job