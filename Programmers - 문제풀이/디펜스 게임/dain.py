from heapq import heappush, heappop

def solution(n, k, enemy):  # 반복되는 정렬 -> heap
    heap = []
    s = 0  # sum
    left = k  # 남은 무적권
    for e in enemy:
        heappush(heap, -e)  # max heap
        s += e
        if s > n:
            if left == 0:
                return len(heap) + k - 1
            else:
                s += heappop(heap)
                left -= 1

    return len(enemy)
