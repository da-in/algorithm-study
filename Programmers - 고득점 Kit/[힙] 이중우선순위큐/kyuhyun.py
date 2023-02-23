import heapq
def solution(operations):
    heap = []

    for ch, num in map(lambda x: x.split(" "), operations):
        num = int(num)
        if ch == 'I':
            heapq.heappush(heap, num)
        else:
            if not heap:
                continue
            if num == -1:
                heapq.heappop(heap)
            else:
                heap.sort()
                heap.pop()

    if not heap:
        return [0, 0]
    return [max(heap), min(heap)]
