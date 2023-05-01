# 야근 피로도 += 남은 작업량^2
# 남은 작업량 = 작업량 - 일한 시간
# 일할 수 있는 시간 = n시간
# 가장 많이 남은 일에서 1씩 빼주자

import heapq

def solution(n,works):
    answer = 0
    heap = []
    
    # 퇴근까지 남은 시간 N이 남은 일의 양보다 많다면 바로 0을 리턴
    if sum(works)<=n:   
        return 0
    
    # 최대힙 구현
    for work in works:
        heapq.heappush(heap,-work)

    # 야근 시간동안
    while n:
        # 가장 많이 남은 작업량을 1씩 줄여준다 (최대힙 구현을 위해 작업량이 음수로 들어가있기 때문에 +1)
        work = heapq.heappop(heap) + 1
        # work가 0이라면 굳이 heap에 다시 넣어주지 않기 위함
        if work != 0:
            # 작업량을 줄인 결과를 다시 heap에 넣어준다
            heapq.heappush(heap,work)
        n -=1

    # 피로도 계산  
    for i in heap:
        # 남은 일의 작업량이 음수로 되어있지만, 제곱을 해주기 때문에 바꿔줄 필요 없음
        answer += i*i
    return answer


#효율성 테스트 시간초과 코드
# def solution(n, works):
#     answer = 0
#     if sum(works)<=n:
#         return answer
    
#     while n:
#         works[works.index(max(works))] -= 1
#         n-=1
        
#     for i in works:
#         answer += i*i
        
#     return answer