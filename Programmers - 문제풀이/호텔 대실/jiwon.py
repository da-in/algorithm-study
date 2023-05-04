from heapq import heapify, heappush, heappop

def solution(book_time):
    # 시간이 겹칠 때 방 +1
    answer = 0
    heap = []
    
    for idx,time in enumerate(book_time):
        start,end = list(map(lambda x:x.split(":"),time))
        start = int(start[0])*60 + int(start[1])
        end = int(end[0])*60 + int(end[1]) + 10
        book_time[idx] = [start,end]
    
    book_time.sort(key = lambda x:x[0])
    first_in = book_time[0][0]
    last_out = sorted(book_time, key = lambda x:-x[1])[0][1]
    
    idx=0
    for time in range(first_in, last_out):
        while idx<len(book_time) and time==book_time[idx][0]:
            heappush(heap, book_time[idx][1])
            idx+=1
        while heap and time==heap[0]:
            heappop(heap)
        if answer<len(heap):
            answer=len(heap)
        
    return answer