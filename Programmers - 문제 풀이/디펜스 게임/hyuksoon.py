from heapq import heappush, heappop
def solution(n, k, enemy):
    h=[]
    for i in range(len(enemy)):
        if len(h)<k:
            heappush(h,enemy[i])
        else:
            if enemy[i]>h[0]:
                temp=heappop(h)
                heappush(h,enemy[i])
            else:
                temp=enemy[i]
            n-=temp
            if n<0:
                return i
    return i+1
    