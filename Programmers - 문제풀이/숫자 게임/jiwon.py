from heapq import heapify, heappop 

def solution(A, B):
    answer = 0
    A.sort()
    heapify(B)
    
    for i in range(len(A)):
        while B:
            b = heappop(B)
            if b>A[i]:
                answer+=1
                break
        
    return answer