from heapq import heappop,heappush
def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    h=[]
    for n in range(len(numbers)):
        while h and h[0][0]<numbers[n]:
            answer[h[0][1]]=numbers[n]
            heappop(h)
        heappush(h,[numbers[n],n])
    return answer