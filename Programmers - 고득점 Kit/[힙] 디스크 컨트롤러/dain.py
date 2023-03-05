from heapq import heappush, heappop

def solution(jobs):
    jobs.sort(reverse=True)
    length = len(jobs)
    answer = t = 0
    heap = []

    for _ in range(length):
        if not heap and t < jobs[-1][0]:
            t = jobs[-1][0]
        while jobs and jobs[-1][0] <= t:
            a, b = jobs.pop()
            heappush(heap, (b, a))
        job = heappop(heap)
        answer += t - job[1] + job[0]
        t += job[0]

    return answer // length
