from collections import deque
import heapq
def solution(jobs):
    jobs.sort()
    answer = 0
    h = []
    length = len(jobs)
    jobs = deque(jobs)
    time = 0
    while jobs or h:
        while jobs and jobs[0][0] <= time:
            temp = jobs.popleft()
            heapq.heappush(h, [temp[1], temp[0]])
        if h:
            now = heapq.heappop(h)
            answer += time+now[0]-now[1]
            time += now[0]
        else:
            time += 1

    answer = answer//length

    return answer