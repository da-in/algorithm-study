def solution(cap, n, deliveries, pickups):
    d, p = n-1, n-1
    min_distance = 0
    while deliveries[d] == 0 and d >= 0:
        d -= 1
    while pickups[p] == 0 and p >= 0:
        p -= 1

    while d >= 0 or p >= 0:
        min_distance += (max(d, p)+1) * 2

        d_cap = cap
        p_cap = cap
        
        while d_cap > 0 and d >= 0:
            if deliveries[d] > d_cap:
                deliveries[d] -= d_cap
                d_cap = 0
            else:
                d_cap -= deliveries[d]
                deliveries[d] = 0
                while deliveries[d] == 0 and d >= 0:
                    d -= 1
        
        while p_cap > 0 and p >= 0:
            if pickups[p] > p_cap:
                pickups[p] -= p_cap
                p_cap = 0
            else:
                p_cap -= pickups[p]
                pickups[p] = 0
                while pickups[p] == 0 and p >= 0:
                    p -= 1

    return min_distance 



case1 = [4, 5, [1, 0, 3, 1 ,2], [0, 3, 0, 4, 0]]
case2 = [2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]]
print(solution(*case1)) # 16
print(solution(*case2)) # 30