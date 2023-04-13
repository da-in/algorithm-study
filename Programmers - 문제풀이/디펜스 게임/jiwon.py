import heapq

def solution(n, k, enemy):
    answer=0
    max_heap=[]
    e_sum=0
    
    for idx, i in enumerate(enemy):
        heapq.heappush(max_heap, (-i,i))
        e_sum+=i
        
        if e_sum>n:
            if k<=0:
                break
            e_sum-=heapq.heappop(max_heap)[1]
            k-=1
        
        answer = idx+1
        
    return answer