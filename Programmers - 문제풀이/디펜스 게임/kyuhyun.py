from heapq import * 
def solution(n, k, enemy):

    answer = 0
    big_enemy = []

    if k >= len(enemy):
        return len(enemy)

    for val in enemy:
        heappush(big_enemy, -val)

        n -= val
        
        if n < 0:
            if k > 0:
                n += -heappop(big_enemy)
                k -= 1
            else:
                break
        answer += 1
    return answer
