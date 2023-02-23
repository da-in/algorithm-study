def main():
    print(solution(25,[2, 14, 11, 21, 17],2))

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()

    start=0
    end=distance
    
    while(start <= end):
        mid=(start+end)//2

        cnt = 0 # 제거할 돌
        i = 0 # 기준 돌
        for j in range(len(rocks)):
            if rocks[j] - i < mid:
                cnt += 1
            else:
                i = rocks[j]
            
            if cnt > n:
                break;


        if cnt <= n:
            start = mid + 1
            answer = mid
        else:
            end = mid -1

    return answer

if __name__ == "__main__":
    main()


    # start=0
    # end=distance
    
    # while(start < end):
    #     mid=start+end//2

    #     if mid < start:
    #         start = mid + 1
    #     else:
    #         end = mid