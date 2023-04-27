from heapq import heapify, heappush, heappop

def solution(n, works):
    answer=0
    if sum(works)<=n:
        return 0
    
#     works = sorted(works)[::-1]
    
#     for _ in range(n):
#         works[0] -= 1
#         works = sorted(works)[::-1]
    
#     for i in works:
#         answer+=i**2

    works = [-work for work in works]
    heapify(works)
    
    while n:
        w = heappop(works)
        heappush(works, w+1)
        n-=1
        
    return sum([work**2 for work in works])