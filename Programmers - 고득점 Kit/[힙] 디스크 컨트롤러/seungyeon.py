import heapq

def main():
    print(solution([[0, 3], [1, 9], [2, 6]]))

def solution(jobs):
    answer = 0
    arr = []
    k,start,end=0,-1,0
    # for i in range(len(jobs)):
    while len(jobs) > k:
        for i in range(len(jobs)):
            if start < jobs[i][0] <= end:
                heapq.heappush(arr, [jobs[i][1],jobs[i][0]])
        if len(arr)>0:
            now = heapq.heappop(arr)
            start = end
            end += now[0]
            answer += (end-now[1])
            k += 1
        else:
            end += 1
        
    return answer//(len(jobs))

# 틀린 예쁜 코드 
# def solution(jobs):
#     answer = 0
#     arr = []
#     for i in range(len(jobs)):
#         heapq.heappush(arr, [jobs[i][0]+jobs[i][1],i])
#     while(arr):
#         answer += jobs[heapq.heappop(arr)[1]][1]
#     return answer//(len(jobs)-1)

if __name__ == "__main__":
    main()