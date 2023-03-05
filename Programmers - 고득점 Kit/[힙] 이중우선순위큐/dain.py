from heapq import heappush, heappop

def solution(operations):
    answer = []
    hq = []
    for o in operations:
        if o[0] == "I":
            heappush(hq, int(o[2:]))
        elif hq:
            if o[2:] == "-1":
                heappop(hq)
            else:
                hq.pop(-1)

    return [0, 0] if len(hq) == 0 else [max(hq), min(hq)]
