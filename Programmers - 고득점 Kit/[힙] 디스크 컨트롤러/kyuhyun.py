import heapq
def solution(jobs):

    work_list = []
    heapq.heapify(jobs)
    n = len(jobs)

    # 가장 먼저 수행하는 작업 불러오기
    req_time, work_time = heapq.heappop(jobs)
    total_time = req_time + work_time
    sum = total_time - req_time

    while jobs or work_list:
      
        if not work_list and jobs[0][0] > total_time:
            req_time, work_time = heapq.heappop(jobs)
            total_time = req_time + work_time
            sum += work_time
        else:
            while jobs and jobs[0][0] <= total_time:
                t, w = heapq.heappop(jobs)
                heapq.heappush(work_list, [w, t])
                
            work_time, req_time = heapq.heappop(work_list)
            total_time += work_time
            sum += (total_time - req_time)

    return sum // n 
    
