#n<enemy[i] = 게임 끝
# 무적권 사용을 언제 해주냐?...
# K가 없을 때 라운드 수 까지 간 뒤 K사용, 게임 다시 진행
# if k==len(enemy) return len(enemy)

from heapq import heappop, heappush
def solution(n, k, enemy):
    answer = 0
    num = 0 #죽인 병사
    heap = []
    
    for i,e in enumerate(enemy):
        num += e
        heappush(heap, -e)
        if num > n:
            if k==0:
                break
            num += heappop(heap)  #죽인 병사 줄어듬
            k -= 1
        answer = i+ 1
    return answer