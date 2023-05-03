# 청소 10분이후 사용 가능
# [대실 시작, 대실 종료]

import heapq

def HtoM(book_time):
    for time in book_time:
        start = time[0].split(':')
        end = time[1].split(':')
        time[0] = int(start[0])*60 + int(start[1])
        time[1] = int(end[0])*60 + int(end[1]) + 10
    

def solution(book_time):
    answer = 0
    heap = []
    
    HtoM(book_time)
    book_time.sort()
    
    print(book_time)
    
    for time in book_time:
        if not heap:
            heapq.heappush(heap, time[1])
            answer += 1
            continue
            
        if heap[0] > time[0]:
            heapq.heappush(heap, time[1])
            answer += 1
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, time[1])
        
    return answer